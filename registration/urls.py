from django.urls import path, reverse_lazy
from .views import *

urlpatterns = [
    path('registration/', register, name='reg'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
