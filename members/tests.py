from django.test import TestCase
from django.urls import reverse

from .models import Member


class MemberManagementTests(TestCase):
    def test_member_search_filters_results(self):
        Member.objects.create(
            first_name="Alice",
            last_name="Johnson",
            email="alice@example.com",
            phone_number="0712345678",
            department="Computer Science",
            registration_number="REG-001",
            status="Active",
        )
        Member.objects.create(
            first_name="Bob",
            last_name="Smith",
            email="bob@example.com",
            phone_number="0723456789",
            department="Mathematics",
            registration_number="REG-002",
            status="Inactive",
        )

        response = self.client.get(reverse("member_list"), {"q": "alice"})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Alice")
        self.assertNotContains(response, "Bob")
