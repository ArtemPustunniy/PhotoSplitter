# PhotoSplitter

## Описание
**PhotoSplitter** — это веб-сервис, разработанный для сортировки и поиска фотографий по лицу с использованием технологий искусственного интеллекта. Сервис позволяет пользователям находить фотографии с их участием среди большого количества снимков, таких как семейные архивы, фотографии с мероприятий и школьных фотосессий. Помимо распознавания лиц, система автоматически фильтрует неподобающий контент и обеспечивает приватность данных.

## Основные функции
- **Распознавание лиц**: ИИ-модель позволяет искать фотографии по лицу, делая поиск удобным и точным.
- **Фильтрация контента**: Классификатор NSFW автоматически фильтрует неподобающий контент, повышая безопасность.
- **Централизованное хранение и управление фотографиями**: Удобное хранение и возможность загрузки архива фотографий.
- **Приватность и контроль доступа**: Настраиваемые опции приватности для частных и корпоративных пользователей.
- **Телеграм-бот**: Возможность отправки уведомлений пользователям через Telegram.

## Технологический стек
- **ML-модели**: YOLOv8 для детекции лиц, ResNet50 и EfficientNetB4 для классификации NSFW-контента, сиамская нейросеть для сравнения лиц.
- **Backend**: Django (Python), MySQL для базы данных.
- **Frontend**: Нативные JavaScript и CSS для простого и понятного интерфейса.
- **Хранение данных**: MySQL, а также файловое хранилище для изображений.
- **Telegram Bot API** для уведомлений.

## Преимущества PhotoSplitter
1. **Бесплатный доступ**: Открытый исходный код и бесплатный доступ к функционалу.
2. **Специализация на мероприятиях**: Возможность поиска по названию и дате мероприятия.
3. **Высокая точность**: Оптимизированные модели для распознавания лиц и фильтрации контента.
4. **Централизованное хранение**: Удобная организация и управление фотографиями по событиям.
5. **Приватность и безопасность**: Настраиваемые параметры конфиденциальности.

## Конкуренты
- **Microsoft Photos**: Неудобная регистрация, поддержка только формата PNG, отсутствие поиска по событиям.
- **Google Photos**: Поиск по лицу недоступен в России.
- **Geometria**: Ограниченный поиск только по их базе данных.

## Установка и запуск
Веб-сервис доступен по домену photosplitter.ru
