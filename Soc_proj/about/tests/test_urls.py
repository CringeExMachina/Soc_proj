from django.test import TestCase, Client


class StaticPageTests(TestCase):
    def setUp(self):
        self.guest_client=Client()
    
    
    def test_about(self):
        response = self.guest_client.get('/about/author/')
        self.assertEqual(response.status_code,200)