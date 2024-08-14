# Import reverse to build URLs based on view names
from django.urls import reverse

# Import APITestCase for testing REST APIs
from rest_framework.test import APITestCase

# Import status to check response status codes
from rest_framework import status

# Import the CustomUser model
from .models import CustomUser


class UserViewTest(APITestCase):
    """
    Test Case for the User views.

    These tests ensure that the API endpoints for creating and managing
    user are working correctly.
    """

    def test_create_user(self):
        """
        Test creating a new user via the API.
        """
        url = reverse("user-create")  # Get the URL for the user creation view
        data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "TestPassword123!",
        }
        # Send a POST request to the URL
        response = self.client.post(url, data, format="json")
        # Check that the response status code is 201 (Created)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Check that the user was created with the correct username and email
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(CustomUser.objects.get().username, "testuser")

    def test_user_detail(self):
        """
        Test retrieving, updating, and deleting a user via the API.
        """
        user = CustomUser.objects.create_user(
            username="testuser", email="test@example.com", password="TestPassword123!"
        )
        # Get the URL for the user detail view
        url = reverse("user-detail", kwargs={"pk": user.pk})

        # Retrieve the user details
        response = self.client.get(url)
        # Check that the user was retrieved successfully
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Update the user details
        data = {"email": "newemail@example.com"}
        response = self.client.patch(url, data, format="json")
        # Check that the user was updated successfully
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(CustomUser.objects.get().email, "newemail@example.com")

        # Delete the user
        response = self.client.delete(url)
        # Check that the user was deleted successfully
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(CustomUser.objects.count(), 0)
