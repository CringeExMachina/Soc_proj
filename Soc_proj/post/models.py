from django.db import models
from django.contrib.auth import get_user_model


class Group(models.Model):
    title = models.TextField()
    adress = models.SlugField()
    description = models.TextField()

    def __str__(self):
        return self.title

        
User = get_user_model()

class Post(models.Model):
    
    def __str__(self):
        return self.text[:15]
    
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        User,
        on_delete= models.CASCADE,
        related_name='posts'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        blank = True,
        null = True,
        related_name='groups'
    )
    image = models.ImageField(
        upload_to='posts/',
        blank=True)

class Comments(models.Model):

    text = models.TextField()
    post = models.ForeignKey(
        Post,
        on_delete = models.CASCADE,
        related_name = 'comments',
    )
    author= models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = 'comments'
    )
    created = models.DateTimeField(auto_now=True)
    
    



    
    
    
    