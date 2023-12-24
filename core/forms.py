from django import forms
from core.models import Post, Comment
from core.models import Category


class NewPostForm(forms.ModelForm):
    """Form layout for writing a new post"""
    cover_image = forms.ImageField(widget=forms.FileInput())

    # Override the __init__ method
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Retrieve categories from the database and create choices list
        categories = Category.objects.all()
        category_choices = [(None, 'Select a category')] + \
            [(category.id, category.cat) for category in categories]

        # Update the choices for the category field
        self.fields['category'].widget.choices = category_choices

    class Meta:
        model = Post
        fields = ['title', 'snippets', 'body',
                  'status', 'cover_image', 'category']

        widgets = {
            'category': forms.Select(attrs={'class': 'form-control form-select text-capitalize'})
        }

        error_messages = {
            'slug': {
                'unique': "This URL already exists!",
                'required': 'The field cannot be empty'
            },
            'title': {
                'required': "Title can't be blanked!"
            }
        }


class EditPostForm(forms.ModelForm):
    """Form layout for writing a new post"""
    cover_image = forms.ImageField(
        required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))

    # Override the __init__ method
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Retrieve categories from the database and create choices list
        categories = Category.objects.all()
        category_choices = [(None, 'Select a category')] + \
            [(category.id, category.cat) for category in categories]

        # Update the choices for the category field
        self.fields['category'].widget.choices = category_choices

    class Meta:
        model = Post
        fields = ['title', 'snippets', 'body',
                  'status', 'category', 'cover_image']

        widgets = {
            'category': forms.Select(attrs={'class': 'form-control form-select text-capitalize'})
        }

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
