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
        labels = {'text': 'Текст комментария', 'post':'Пост', 'author':'Автор','created':'Дата создания'}
        fields=('text','post','author')