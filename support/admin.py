from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin import ModelAdmin
from .models import *

from .models import Users, Events


class EventsAdmin(ModelAdmin):
    list_display = (['user', 'eventname', 'description', 'eventdate', 'location', 'likes', 'file_archive', 'private_mode'])
    verbose_name = 'Events'


class PathToEventsFilesAdmin(ModelAdmin):
    list_display = (['path_to_unarchive_file', 'id_of_event', 'id_of_user', 'clear_name_of_archive', 'type_of_archive'])
    verbose_name = 'PathToEventsFiles'


class UserIdentificationPhotosAdmin(ModelAdmin):
    list_display = (['user_id', 'identification_photo_1', 'identification_photo_2'])
    verbose_name = 'UserIdentificationPhotos'


class HeadbandsAdmin(ModelAdmin):
    list_display = (['headband'])
    verbose_name = 'EventHeadbands'


class PathToArchiveReleaseAdmin(ModelAdmin):
    list_display = (['path_to_release_archive'])
    verbose_name = 'PathToArchiveReleaseFiles'


class PathToArchiveReleaseOnePersonPhotosAdmin(ModelAdmin):
    list_display = (['path_to_release_archive'])
    verbose_name = 'PathToArchiveReleaseFilesOnePerson'


class UsersInline(admin.StackedInline):
    model = Users
    can_delete = False
    list_display = (['user', 'email', 'first_name', 'last_name',])
    verbose_name = 'Users'


class CustomizedUsers(UserAdmin):
    inlines = (UsersInline, )


admin.site.unregister(User)
admin.site.register(User, CustomizedUsers)
admin.site.register(Events, EventsAdmin)
admin.site.register(Headbands, HeadbandsAdmin)
admin.site.register(PathToArchiveRelease, PathToArchiveReleaseAdmin)
admin.site.register(PathToArchiveReleaseOnePeoplePhotos, PathToArchiveReleaseOnePersonPhotosAdmin)
admin.site.register(PathToEventsFiles, PathToEventsFilesAdmin)
admin.site.register(UsersIdentificationphotos, UserIdentificationPhotosAdmin)
admin.site.site_titlle = 'Admin-pannel PhotoSplitter'
admin.site.site_header = 'Admin-pannel PhotoSplitter'
