from django.test import TestCase, Client
from django.contrib.auth.models import User


from ..models import Post,Group


class StaticURLTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='auth')
        cls.group = Group.objects.create(
            title='Str',
            adress='Slug',
            description='Desc',  
        )
        cls.post=Post.objects.create(
            author=cls.user,
            text='Тестовая группа',
        )
    
    def setUp(self):
        # Устанавливаем данные для тестирования
        # Создаём экземпляр клиента. Он неавторизован.
        self.guest_client = Client()
        self.user=User.objects.create_user(username='blank')
        self.authorized_client=Client()
        self.authorized_client.force_login(self.user)
        

    def test_homepage(self):
        # Отправляем запрос через client,
        # созданный в setUp()
        response = self.authorized_client.get('/')  
        self.assertEqual(response.status_code, 200)
    
    def test_homepage_redirect_anonymouse(self):
        response = self.guest_client.get('/',follow=True)
        self.assertRedirects(response,('/auth/login/?next=/'))
        
    def test_group_page(self):
        response=self.authorized_client.get('/group/Slug/')
        self.assertEqual(response.status_code,200)
    
    def test_profile_page(self):
        response=self.authorized_client.get('/profile/blank/')
        self.assertEqual(response.status_code,200)
    
    def test_post_page(self):
        response=self.guest_client.get('/posts/1/')
        self.assertEqual(response.status_code,200)
        