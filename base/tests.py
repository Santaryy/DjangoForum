from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


class UserCreationTest(TestCase):
    def setUp(self):
        user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
            'name': 'Test User',
            'bio': 'This is a test user bio.'
        }
        
        self.client.post(reverse('register'), user_data)
    
    def test_create_user(self):
        User = get_user_model()
        user_data = {
            'username': 'testuser1',
            'email': 'testuser1@example.com',
            'password1': 'testpassword1234',
            'password2': 'testpassword1234',
            'name': 'Test User Register',
            'bio': 'This is a test user bio.'
        }

        response = self.client.post(reverse('register'), user_data)

        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='testuser').exists())
        self.assertRedirects(response, reverse('home'))
        
    def test_create_user_with_invalid_data(self):
        User = get_user_model()
        user_data = {
            'username': 'testuser2',
            'password1': 'testpassword12345',
            'password2': 'testpassword12345',
            'name': 'Test User 2',
            'bio': 'This is a test user bio.'
        }

        response = self.client.post(reverse('register'), user_data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(User.objects.filter(username='testuser2').exists())
        
    def test_valid_login(self):
        login_data = {
            'email': 'testuser@example.com',
            'password': 'testpassword123',
        }
        response = self.client.post(reverse('login'), login_data)
        self.assertRedirects(response, reverse('home'))
        
        
    def test_login_invalid_user(self):
        invalid_login_data = {
            'email': 'invalid@example.com',
            'password': 'invalidpassword',
        }

        response = self.client.post(reverse('login'), invalid_login_data)
        not self.assertRedirects(response, reverse('home'))
        

    
