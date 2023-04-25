from django.shortcuts import redirect
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy, reverse
from django.contrib.auth import views as auth_view
from django.contrib import messages
from django.contrib.auth import get_user_model
from .forms import RegistrationForm, LoginForm, EditUserForm

User = get_user_model()

class UserRegisterView(CreateView):
    """
    Using django's User creation form with the generic create view
    for registeration.
    """
    form_class = RegistrationForm
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
    
    form_class = LoginForm
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
    """Update view for editing the user profile."""
    form_class = EditUserForm
    template_name = 'accounts/settings.html'
    success_url = reverse_lazy('accounts:settings')

    def get_object(self):
        """We use get object to return the current logged in user."""
        return self.request.user
    
    def form_valid(self, form):
        self.object.save()
        messages.success(self.request, "Changes made Successfully!")

        return super().form_valid(form)