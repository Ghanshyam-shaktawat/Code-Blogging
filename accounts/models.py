from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

GENDER = [
    ('n', 'not specified'),
    ('f', 'female'),
    ('m', 'male')
]

class MyUserModel(AbstractUser):
    first_name = None
    last_name = None
    full_name = models.CharField(max_length=64, blank=True)
    email = models.EmailField(_("Email"))
    gender = models.CharField(max_length=10, choices=GENDER, default='n')
    bio = models.CharField(max_length=200, blank=True, null=True)
    website_link = models.CharField(max_length=100, blank=True, null=True)
    display_email = models.BooleanField(default=False)
    pfp = models.ImageField(upload_to='images/users/', default="../media/images/users/default.jpg", null=True)

def __str__(self):
    return self.username