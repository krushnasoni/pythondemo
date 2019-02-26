from django import forms
from .models import Post

class BlogForm(forms.ModelForm):

    class Meta:
            model = Post
            fields = ('author', 'title', 'text', 'sub_title')