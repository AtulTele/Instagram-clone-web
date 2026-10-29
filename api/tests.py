
from django.test import SimpleTestCase
from django.urls import resolve

from api.views import SignupAPIView


class SignupAPIURLTests(SimpleTestCase):
    """Verify that the API signup URL points to the expected view."""

    def test_signup_api_url_resolves(self):
        match = resolve("/api/auth/signup")
        self.assertEqual(match.func.view_class, SignupAPIView)
