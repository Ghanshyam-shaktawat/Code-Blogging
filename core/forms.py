from django import forms
from core.models import Post, Comment

class NewPostForm(forms.ModelForm):
    """Form layout for writing a new post"""
    cover_image = forms.ImageField(widget=forms.FileInput())

    class Meta:
        model = Post
        fields = ['title', 'snippets', 'body', 'status', 'slug', 'cover_image']

        error_messages = {
            'slug': {
                'unique': "This url already exists!",
                'required': 'The field cannot be empty'
            },

            'title': {
                'required': "Title can't be blanked!"
            }
        }


class CommentForm(forms.ModelForm):
    """Form for making comment on the post by authenticated user"""
    class Meta:
        model = Comment
        fields = ['body']