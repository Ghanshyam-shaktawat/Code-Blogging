from django.urls import path
from accounts.views import UserRegisterView, LoginView, EditUserProfile

app_name = 'accounts'
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('settings/', EditUserProfile.as_view(), name='settings'),
]