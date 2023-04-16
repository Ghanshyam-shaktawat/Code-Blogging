from django.contrib import admin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'status', 'created_on']
    list_filter = ['status']
    prepopulated_fields = {'slug': ('title',)}

class AdminComment(admin.ModelAdmin):
    list_display = ['post', 'user']

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, AdminComment)

