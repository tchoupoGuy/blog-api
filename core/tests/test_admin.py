from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse



class AdminSiteTests(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().create_user(
            email = 'admin@guyblog.com',
            password='password123'
            
        )
        self.client.force_login(self.admin_user)
        self.user=get_user_model().objects.create_user(
            email='test@guyblog.com',
            password='password123',
            name='Test user full name'
            
        )
       
    


