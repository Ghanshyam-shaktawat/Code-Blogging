from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import MyUserModel


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = MyUserModel
        fields = ('username',)

class CustomUserChangeForm(UserChangeForm):
    username = forms.CharField(required=True, label="Your Username")
    email = forms.EmailField(required=True, label="Your Email")
    display_email = forms.BooleanField(required=False, label="Display email on profile")
    first_name = forms.CharField(label="First Name")
    last_name = forms.CharField(label="Last Name")
    password = None

    class Meta:
        model = MyUserModel
        fields = ('first_name', 'last_name', 'username', 'email', 'display_email', 'bio', 'gender')