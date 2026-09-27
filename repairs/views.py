from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import TicketForm
from .models import Ticket


@login_required
def ticket_list(request):
    if request.method == "POST":
        form = TicketForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("ticket_list")
    else:
        form = TicketForm()

    search = request.GET.get("q", "").strip()
    tickets = Ticket.objects.order_by("-created_at")

    if search:
        tickets = tickets.filter(
            Q(device__icontains=search)
            | Q(problem__icontains=search)
        )

    return render(
        request,
        "repairs/ticket_list.html",
        {
            "tickets": tickets,
            "form": form,
            "search": search,
            "status_choices": Ticket.STATUS_CHOICES,
        },
    )


@login_required
@require_POST
def update_status(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    new_status = request.POST.get("status")
    valid_statuses = dict(Ticket.STATUS_CHOICES)

    if new_status in valid_statuses:
        ticket.status = new_status
        ticket.save(update_fields=["status"])

    return redirect("ticket_list")