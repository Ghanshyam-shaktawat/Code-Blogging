from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import MyUserModel
from django.contrib.auth import get_user_model


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Your Email', widget=forms.EmailInput(attrs={'class':'field', 'placeholder':'Your Email'}))
    full_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'field', 'placeholder':'Your Full Name'}))
    
    class Meta:
        model = get_user_model()
        fields = ('username','email', 'full_name', 'password1', 'password2')
        error_messages = {
            'username':{
                'unique': 'This username already exists. Try something else!',
                'required' : 'Enter your username'
                }
        }
        
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'field'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password1'].widget.attrs['class'] = 'field'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['class'] = 'field'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'


class LoginForm(AuthenticationForm):
    username = forms.CharField()

class EditUserForm(UserChangeForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))
    display_email = forms.CharField(required=False, widget=forms.CheckboxInput(attrs={'class':''}))
    full_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    bio = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control'}))
    website_link = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    pfp = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class':'form-control'}))

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'display_email', 'full_name', 'bio', 'gender', 'pfp')