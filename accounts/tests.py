from django.test import TestCase
from django.urls import reverse


class LoginViewTests(TestCase):
    def test_invalid_credentials_display_an_error(self):
        response = self.client.post(
            reverse("login"),
            {"username": "missing-user", "password": "wrong-password"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            "Please enter a correct username and password",
        )
        self.assertContains(response, 'role="alert"')
