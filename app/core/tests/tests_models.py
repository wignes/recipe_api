from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Create test case """

    def test_create_user_with_email_successful(self):
        """Test create user with email successful event"""
        email = "test@gmail.com"
        password = "test12344"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test new user email is normalized"""
        email = "test@GMAIL>COM"
        user = get_user_model().objects.create_user(email, 'test1234')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test new user invalid email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test1234')

    def test_new_create_super_user(self):
        """ Test creating new super user"""
        user = get_user_model().objects.create_superuser(
            'test@gmail.com',
            'test1234'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
