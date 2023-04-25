from django.contrib.auth.models import User
from django.test import TestCase,Client
from django.urls import reverse


from post.models import Post,Group

class PostViewsTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='auth')
        cls.group = Group.objects.create(
            title='Тестовая группа',
            adress='test',
            description='Тестовое описание',  
        )
        cls.post=Post.objects.create(
            author=cls.user,
            text='Тестовая группа',
        )
        
    def setUp(self):
        # Создаем авторизованный клиент
        self.user = User.objects.create_user(username='blank')
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)
        
    def test_homepage(self):
        response = self.authorized_client.get(reverse('post:General'))
        self.assertTemplateUsed(response,'post/index.html')
    
    def test_group_page(self):
        response = self.authorized_client.get('/group/test/')
        self.assertTemplateUsed(response,'post/group_post.html')