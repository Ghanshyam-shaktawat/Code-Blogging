from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length= 255)
    snippets = models.CharField(max_length=120)
    body = models.TextField()
    pub_date = models.DateTimeField('Date Published', auto_now_add=True)
    
    def __str__(self):
        return self.title