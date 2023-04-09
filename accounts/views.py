from django.shortcuts import redirect
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth import views as auth_view
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import MyUserModel

User = get_user_model()

class UserRegisterView(CreateView):
    """
    Using django's User creation form with the generic create view
    for registeration.
    """
    form_class = CustomUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:login')

    def dispatch(self, request, *args, **kwargs):
        """
        This method let's us redirect already logged in user to homepage.
        And dont allow them to visit the login page until logged out.
        """        
        if request.user.is_authenticated:
            return redirect(reverse('core:index'))
        return super(UserRegisterView, self).dispatch(request, *args, **kwargs)


class LoginView(auth_view.LoginView):
    """django's Login view for logging users"""
    
    form_class = AuthenticationForm
    template_name= 'accounts/login.html'
    
    def dispatch(self, request, *args, **kwargs):
        """
        This method let's us redirect already logged in user to homepage.
        And dont allow them to visit the login page until logged out.
        """
        if request.user.is_authenticated:
            return redirect(reverse('core:index'))
        return super(LoginView, self).dispatch(request, *args, **kwargs)
    

class EditUserProfile(UpdateView):
    form_class = CustomUserChangeForm
    template_name = 'accounts/settings.html'
    success_url = reverse_lazy('accounts:settings')

    def get_object(self):
        return self.request.user