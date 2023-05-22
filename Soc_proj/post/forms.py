from django import forms
from .models import Post,Comments

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        labels = {'group': 'Группа', 'text': 'Сообщение', 'image':'Картинка'}
        fields=('text','group','image')
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields=('text','post','author')