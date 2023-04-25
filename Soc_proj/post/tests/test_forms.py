from django.test import Client,TestCase
from django.urls import reverse
from django.contrib.auth.models import User


from post.forms import PostForm
from ..models import Post,Group


class PostCreateFormTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='auth')
        cls.group = Group.objects.create(
            title='Тестовая группа',
            adress='Тестовый слаг',
            description='Тестовое описание',  
        )
        cls.post=Post.objects.create(
            author=cls.user,
            text='Тестовая группа',
        )
        
    def setUp(self):
         self.authorized_client=Client()
         self.authorized_client.force_login(self.user)
       
        
    def testik(self):
        post_count=Post.objects.count()
        
        form_data = {
            'title':'Тестовая група',
            'adress':'Тестовый саг',
            'description':'Тестовое оисание',
            'author':'{cls.user}',
            'text':'test'
        }
        
        response=self.authorized_client.post(reverse('post:post_create'),
        data=form_data,
        follow=True
        )
        
        self.assertEqual(Post.objects.count(), post_count+1)
        