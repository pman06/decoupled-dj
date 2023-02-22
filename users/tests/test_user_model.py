from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class CreateUserTest(TestCase):
    """"Test that the user is created successfully."""
    
    def setUp(self):
        self.email = "mytest@gmail.com"
        self.username = "myname"
        self.password = "myTestPass"
        self.new_user = User.objects.create_user(
            email=self.email,
            username=self.username,
            password=self.password
		)
    
    def test_create_user(self):
        """"Test normal user was created"""      
        self.assertEqual(self.new_user.email, self.email)
        self.assertEqual(self.new_user.username, self.username)
    