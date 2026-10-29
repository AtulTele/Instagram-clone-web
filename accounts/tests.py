
from django.test import SimpleTestCase
from django.urls import reverse, resolve

from accounts.views import UserLogin, SignupView


class AccountURLTests(SimpleTestCase):
    """Test account URL routing without creating database records."""

    def test_login_url_resolves(self):
        match = resolve("/auth/login/")
        self.assertEqual(match.func.view_class, UserLogin)

    def test_signup_url_resolves(self):
        match = resolve("/auth/create-account/")
        self.assertEqual(match.func.view_class, SignupView)


class AccountPageTests(SimpleTestCase):
    """Test that public account pages respond successfully."""

    def test_login_page_returns_success(self):
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)

    def test_signup_page_returns_success(self):
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)
