from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Ticket


class TicketTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="test-password-123",
        )

        self.ticket = Ticket.objects.create(
            device="Dell laptop",
            problem="Will not turn on",
        )

    def test_signed_out_visitor_cannot_view_tickets(self):
        response = self.client.get(reverse("ticket_list"))

        self.assertRedirects(
            response,
            reverse("login") + "?next=" + reverse("ticket_list"),
        )

    def test_signed_in_user_can_update_status(self):
        self.client.force_login(self.user)

        response = self.client.post(
            reverse("update_status", args=[self.ticket.id]),
            {"status": "Completed"},
        )

        self.ticket.refresh_from_db()

        self.assertEqual(self.ticket.status, "Completed")
        self.assertRedirects(response, reverse("ticket_list"))