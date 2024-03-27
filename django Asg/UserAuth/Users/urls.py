from django.urls import path
from .views import *

urlpatterns = [
    path('register/', user_registration, name='user_registration'),
    path('verify/', user_verification, name='user_verification'),
    path('login/', user_login, name='user_login'),
    path('forgot_password/', forgot_password, name='forgot_password'),
    path('reset_password/', reset_password, name='reset_password'),
]
