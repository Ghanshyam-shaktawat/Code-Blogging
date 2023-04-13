from django.db import models
from django.contrib.auth import get_user_model
from core.models import Post

User = get_user_model()

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=200)
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s commented by- %s' % (self.post.title, self.user)
