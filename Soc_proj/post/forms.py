from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        labels = {'group': 'Группа', 'text': 'Сообщение'}
        fields=('text','group')