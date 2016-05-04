from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.test import APITestCase


class UnAuthSecurityTests(APITestCase):
    """Test Security without auth."""

    def test_access_user(self):
        c = APIClient()
        response = c.post('/users/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_access_specific_user(self):
        c = APIClient()
        response = c.post('/users/1')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_access_profile(self):
        c = APIClient()
        response = c.post('/profiles/1')
        self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)

    def test_access_route(self):
        
