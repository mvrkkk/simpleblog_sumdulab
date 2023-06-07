from django import forms
from .models import Post, Comment
from tinymce.widgets import TinyMCE

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'body': TinyMCE()
        }
        exclude = ['user', 'created_at']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        widgets = {
            'body': TinyMCE()
        }