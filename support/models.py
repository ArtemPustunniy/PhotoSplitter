import os
from django.db import models
from django.core.validators import FileExtensionValidator, EmailValidator
from django.contrib.auth.models import User


class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    email = models.EmailField(unique=True, default=None, validators=[EmailValidator(message='Invalid email')])
    first_name = models.CharField(max_length=50, default=None)
    last_name = models.CharField(max_length=50, default=None)

    def __str__(self):
        return self.user.first_name


def users_identification_photos_path(instance, filename):
    return os.path.join('upload_user_files', str(instance.user.id), filename)


def events_path(instance, archive_name):
    return os.path.join('upload_event_files', str(instance.user.id), archive_name)


def events_headbands_path(instance, photo_name):
    print(instance)
    return os.path.join('headbands_of_events', str(instance.event.id), photo_name)


class UsersIdentificationphotos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    identification_photo_1 = models.ImageField(upload_to=users_identification_photos_path, default=None, blank=True)
    identification_photo_2 = models.ImageField(upload_to=users_identification_photos_path, default=None, blank=True)
    # id_of_user = models.IntegerField(default=None)


class UsersSavedArchives(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    saved_file_archive = models.FileField(upload_to='upload_user_files')


class Events(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    eventname = models.CharField(max_length=50)
    description = models.TextField(max_length=150)
    eventdate = models.CharField(max_length=30)
    location = models.CharField(max_length=150)
    likes = models.IntegerField(default=0)
    file_archive = models.FileField(upload_to=events_path, validators=[FileExtensionValidator(allowed_extensions=['zip', 'rar', 'gz'])])
    password = models.CharField(max_length=30, blank=True)
    unique_link = models.URLField(blank=True)
    private_mode = models.BooleanField(default=False)


class EventLikes(models.Model):
    event_id = models.IntegerField()
    user_id = models.IntegerField()


class PathToEventsFiles(models.Model):
    path_to_unarchive_file = models.CharField(max_length=150)
    id_of_event = models.IntegerField()
    id_of_user = models.IntegerField()
    clear_name_of_archive = models.CharField(max_length=150, default=None)
    type_of_archive = models.CharField(max_length=150, default=None)


class PathToArchiveRelease(models.Model):
    path_to_release_archive = models.FileField()
    event_id = models.IntegerField()


class PathToArchiveReleaseOnePeoplePhotos(models.Model):
    path_to_release_archive = models.FileField()
    event_id = models.IntegerField()
    user_id = models.IntegerField()


class Headbands(models.Model):
    event = models.ForeignKey(Events, on_delete=models.CASCADE, default=None)
    headband = models.ImageField(upload_to=events_headbands_path)


class EventParticipation(models.Model):
    event_id = models.IntegerField()
    user_id = models.IntegerField()





