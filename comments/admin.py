from django.contrib import admin
from .models import Comment

class AdminComment(admin.ModelAdmin):
    list_display = ['body', 'post', 'user']

admin.site.register(Comment, AdminComment)
