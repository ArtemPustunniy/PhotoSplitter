import os
import shutil

from PIL import Image
from ultralytics import YOLO

from tqdm import tqdm

import torch
import torchvision.transforms as transforms
from torchvision import models

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def load_model_nude(model_path, model_name, device):
    if model_name == "resnet":
        model = models.resnet50(pretrained=False)
        num_ftrs = model.fc.in_features
        model.fc = torch.nn.Sequential(
            torch.nn.Dropout(0.3),
            torch.nn.Linear(num_ftrs, 2)
        )
    elif model_name == "efficientnet":
        model = models.efficientnet_b0(pretrained=False)
        num_ftrs = model.classifier[1].in_features
        model.classifier = torch.nn.Sequential(
            torch.nn.Dropout(0.3),
            torch.nn.Linear(num_ftrs, 2)
        )

    model.load_state_dict(torch.load(model_path, map_location=torch.device("cpu")))
    model.eval()
    return model


def predict_nude(model, image_path, device):
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])

    image = Image.open(image_path).convert('RGB')
    image = transform(image).unsqueeze(0).to(device)

    with torch.no_grad():
        outputs = model(image)
        probs = torch.nn.functional.softmax(outputs, dim=1)
        top_p, top_class = probs.topk(1, dim=1)

    return top_class.item(), top_p.item()


def process_images_nude(folder_path, model_path, model_name, device):
    model = load_model_nude(model_path, model_name, device).to(device)
    results = []

    for root, dirs, files in os.walk(folder_path):
        for file in tqdm(files):
            if file.lower().endswith(('png', 'jpg', 'jpeg')):
                image_path = os.path.join(root, file)
                pred_class, prob = predict_nude(model, image_path, device)
                if pred_class == 0 and prob > 0.8:  # 0 - nudes
                    results.append((image_path, prob))

    return results


def faces_cutting(DATA_PATH):
    MODEL = YOLO(os.path.join(BASE_DIR, "ml_part/face_detection_without_cutout_best.pt"))

    FINAL_PATH = f"{DATA_PATH}_cutted"

    if os.path.exists(FINAL_PATH):
        pass
    else:
        os.makedirs(FINAL_PATH)

    for root, dirs, files in os.walk(DATA_PATH):
        for file in files:
            if file.lower().endswith((".png", ".jpg", ".jpeg", ".heif", ".gif", ".bmp")):
                filename_with_ext = os.path.join(root, file)
                filename, ext = os.path.splitext(file)
                image = Image.open(filename_with_ext)

                results = MODEL.predict(image, verbose=False, conf=0.6)

                if len(results[0].boxes.xyxy.tolist()) == 0:
                    continue

                image_folder = os.path.join(FINAL_PATH, f"{filename}")
                os.makedirs(os.path.join(image_folder))

                counter_filename = 1
                for result in results[0].boxes.xyxy.tolist():
                    x1, y1, x2, y2 = result[0], result[1], result[2], result[3]
                    face_image = image
                    face = face_image.crop((x1, y1, x2, y2))

                    if face.mode == "RGBA":
                        face = face.convert("RGB")

                    image_name, image_ext = os.path.splitext(file)
                    new_image_name = os.path.join(
                        image_folder, f"{image_name}_{counter_filename}"
                    )

                    face.save(new_image_name + image_ext)

                    counter_filename += 1


class SiameseNetwork(torch.nn.Module):
    def __init__(self):
        super(SiameseNetwork, self).__init__()
        self.backbone = models.resnet50(weights=models.resnet.ResNet50_Weights.IMAGENET1K_V1)
        self.backbone.fc = torch.nn.Sequential(
            torch.nn.Linear(self.backbone.fc.in_features, 2048),
            torch.nn.BatchNorm1d(2048),
            torch.nn.LeakyReLU(inplace=True),
            torch.nn.Dropout(p=0.2),
            torch.nn.Linear(2048, 1024),
            torch.nn.BatchNorm1d(1024),
            torch.nn.LeakyReLU(inplace=True),
            torch.nn.Dropout(p=0.1),
            torch.nn.Linear(1024, 512),
            torch.nn.BatchNorm1d(512),
            torch.nn.LeakyReLU(inplace=True),
            torch.nn.Dropout(p=0.1),
            torch.nn.Linear(512, 256),
            torch.nn.BatchNorm1d(256),
            torch.nn.LeakyReLU(inplace=True),
            torch.nn.Linear(256, 128),
            torch.nn.BatchNorm1d(128),
            torch.nn.LeakyReLU(inplace=True),
        )

    def forward(self, x):
        x = self.backbone(x)
        return x


def load_model_siamse(model_path, device):
    model = SiameseNetwork().to(device)
    model.load_state_dict(torch.load(model_path, map_location=device))
    model.eval()
    return model


def preprocess_image_siamse(image_path, transform):
    image = Image.open(image_path).convert("RGB")
    image = transform(image)
    return image.unsqueeze(0)


def get_embedding_siamse(model, image_tensor, device):
    with torch.no_grad():
        embedding = model.backbone(image_tensor.to(device))
    return embedding


def compare_images_siamse(model, target_image_path, folder_path, transform, device, threshold=0.5):
    target_image_tensor = preprocess_image_siamse(target_image_path, transform)
    target_embedding = get_embedding_siamse(model, target_image_tensor, device)

    similarities = []
    for folder, subfolders, files in os.walk(folder_path):
        for file in files:
            temp = str(folder)[str(folder).rfind('\\') + 1:]
            image_path = os.path.join(folder_path, f"{temp}/{file}")
            image_tensor = preprocess_image_siamse(image_path, transform)
            image_embedding = get_embedding_siamse(model, image_tensor, device)

            cos = torch.nn.CosineSimilarity(dim=1, eps=1e-6)
            similarity = cos(target_embedding, image_embedding).item()
            filename, ext = os.path.splitext(file)
            image_name = filename.split("_")[0]
            new_folder = str(folder).replace("_cutted", "")
            similarities.append((os.path.join(new_folder[0:new_folder.rfind('\\')], image_name + ext), similarity))
            # similarities.append((os.path.join((str(folder)[str(folder).rfind('/'):0]), (str(folder)[str(folder).rfind('/'):str(folder).rfind('\\')]).replace('_cutted', ''), f"{str(file).split('_')[0]}.{str(file).split('_')[1].split('.')[1]}"), similarity))
            #similarities.append()

    similar_images = [name for name, sim in similarities if sim > threshold]
    return similar_images
