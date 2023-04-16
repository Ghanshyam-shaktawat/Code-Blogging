from django import forms
from core.models import Post, Comment

class NewPostForm(forms.ModelForm):
    """Form layout for writing a new post"""
    class Meta:
        model = Post
        fields = ['title', 'body', 'slug', 'snippets', 'status']


class CommentForm(forms.ModelForm):
    """Form for making comment on the post by authenticated user"""
    class Meta:
        model = Comment
        fields = ['body']