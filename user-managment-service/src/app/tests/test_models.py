# Import Django's test case class for unit testing
from django.test import TestCase

# Import the function to get the current user model
from django.contrib.auth import get_user_model


class CustomUserModelTest(TestCase):
    """
    Test Case for the CustomUser model.

    This test verifies that we can create a user with username and eamil,
    and that the string representation of the user is correct.
    """

    def test_create_user(self):
        """
        Test creating a user instance.
        """
        User = get_user_model()  # Get the current user model (CustomUser)
        user = User.objects.create_user(
            username="testuser", email="test@example.com", password="TestPassword123!"
        )
        # Check that the user was created wiht the correct username and email
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "test@exmaple.com")

        # Check that the user's password is stored securely
        self.assertTrue(user.check_password("TestPassword123!"))

    def test_user_string_representation(self):
        """
        Test the string representation of the User model.
        """
        User = get_user_model()
        user = User(username="testuser", email="test@example.com")
        # Check that the string representation is the username
        self.assertEqual(str(user), user.username)
