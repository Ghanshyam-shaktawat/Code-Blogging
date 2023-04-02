from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

STATUS = [
    (0, 'draft'),
    (1, 'publish')
]


# class Author(AbstractUser):
#     """
#     Using predefined user model and overriding and adding new filds to user model
#     """
#     email = models.EmailField(_("Email"), unique=True, max_length=70)

class Post(models.Model):
    """Model for Blog Post"""
    title = models.CharField(max_length=200)
    snippets = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, max_length=200, null=False, help_text="Post unique url")
    body = models.TextField()
    created_on = models.DateTimeField('Date Published')
    status = models.IntegerField(choices=STATUS, default=0)
    
    def __str__(self):
        return self.title