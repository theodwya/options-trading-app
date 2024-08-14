from django.test import TestCase  # Import Django's test case class
from .serializers import UserSerializer  # Import the serializer to be tested
from .models import CustomUser  # Import the CustomUser model


class UserSerializerTest(TestCase):
    """
    Test Case for the UserSerializer.

    This test verifies that the serializer correctly serializes a
    user instance into JSON and that it correctly deserializes JSON
    data into a user instance.
    """

    def test_serialization(self):
        """
        Test serializing a user instance into JSON.
        """
        user = CustomUser(username="testuser", email="test@example.com")
        serializer = UserSerializer(user)  # Serialize the user instance
        data = serializer.data  # Get the serialized data
        # Check that the serialized dat contains the correct fields and values
        self.assertEqual(data["username"], "testuser")
        self.assertEqual(data["email"], "test@example.com")

    def test_deserialization(self):
        """
        Test deserializing JSON data into a user instance.
        """
        data = {"username": "testuser", "email": "test@example.com"}
        serializer = UserSerializer(data=data)  # Deserialize the JSON data
        self.assertTrue(serializer.is_valid())  # Check that the data is valid
        # Save the deserialized data to create a user instance
        user = serializer.save()
        # Check that the user instance was created with the correct
        # username and email
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "test@example.com")
