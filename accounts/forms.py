from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import MyUserModel
from django.contrib.auth import get_user_model


class RegistrationForm(UserCreationForm):
    class Meta:
        model = MyUserModel
        fields = ('username',)

class LoginForm(AuthenticationForm):
    username = forms.CharField()

class EditUserForm(UserChangeForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-field'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class':'form-field'}))
    display_email = forms.CharField(required=False, widget=forms.CheckboxInput(attrs={'class':'form-field'}))
    full_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-field'}))
    bio = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-field'}))
    website_link = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-field'}))

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'display_email', 'full_name', 'bio', 'gender')