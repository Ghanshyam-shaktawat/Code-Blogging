from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.contrib.auth.models import User

STATUS = [
    (0, 'draft'),
    (1, 'publish')
]    

class Post(models.Model):
    """Model for Blog Post"""
    title = models.CharField(max_length=200)
    snippets = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, max_length=200, null=False, help_text="Post unique url")
    body = models.TextField()
    created_on = models.DateTimeField('Date Published', auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        """It redirects to the detail page after an database entry"""
        return reverse('core:detail', args=[str(self.user.username), str(self.slug)])