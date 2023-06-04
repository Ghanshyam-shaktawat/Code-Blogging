from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from bloggingApp.util import unique_slug_generator
from django.conf import settings
User = settings.AUTH_USER_MODEL

STATUS = [
    (0, 'draft'),
    (1, 'publish'),
]

class Category(models.Model):
    """Making category for blogs"""
    cat = models.CharField("Post's Category", max_length=125, unique=True, blank=True)

    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.cat
    
    def save(self, *args, **kwargs):
        self.cat = self.cat.lower()
        return super(Category, self).save(*args, **kwargs)


class Post(models.Model):
    """Model for Blog Post"""
    title = models.CharField(max_length=200)
    snippets = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, max_length=200, null=False, help_text="Post unique url")
    body = models.TextField()
    created_on = models.DateTimeField('Date Published', auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, max_length=125, related_name='p_category')
    cover_image = models.ImageField(upload_to='images/post/', null=True, blank=True)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)
    
    def __str__(self):
        return self.title
    
    def total_likes(self):
        return self.likes.count()
    
    def get_absolute_url(self):
        """It redirects to the detail page after an database entry"""
        return reverse('core:detail', args=[str(self.user.username), str(self.slug)])

@receiver(pre_save, sender=Post)
def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=200)
    comment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-comment_date']

    def __str__(self):
        return '%s commented by- %s' % (self.post.title, self.user)
    
class Bookmark(models.Model):
    bookmark_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    bookmark_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookmarks')
