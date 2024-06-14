from django.urls import path
from .views import user_login, register_view, custom_logout

urlpatterns=[
    path('login/', user_login, name='login'),
    path('accounts/login/', user_login, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', custom_logout, name='logout'),
]