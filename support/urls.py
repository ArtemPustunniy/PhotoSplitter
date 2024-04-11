from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from django.urls import path, include, reverse_lazy
from .views import *

urlpatterns = [
    path('', main_page, name='main'),
    path('auth/', include('registration.urls')),
    path('reset/', include('reset_password.urls')),
    path('ml_part/', include('ml_part.urls')),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('find/',  search_events_paginator, name='find'),
    path('profile/', go_profile, name='profile'),
    path('download_all_zip/<int:event_id>', download_all_zip, name='download_all_zip'),
    path('download_my_zip/<int:event_id>', download_my_zip, name='download_my_zip'),
    path('confirm_password/<int:event_id>', confirm_password, name='confirm_password'),
    path('add_event/', add_event, name='add_event'),
    path('add_photo/', add_profile_photos, name='add_photo'),
    path('change_photo/', change_profile_photos, name='change_photo'),
    path('add_preview/<int:event_id>', add_preview_photos, name='add_preview'),
    path('change_preview/<int:event_id>', change_preview_photos, name='change_preview'),
    path('detail_events/<int:event_id>', view_detail_events, name='detail_events'),

]

