from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .models import Notification


@login_required
def notification_list(request):
    notifications = Notification.objects.filter(
        recipient=request.user
    )

    return render(
        request,
        "notifications/notification_list.html",
        {
            "notifications": notifications,
        },
    )


@login_required
def mark_notification_read(request, pk):
    notification = get_object_or_404(
        Notification,
        pk=pk,
        recipient=request.user,
    )

    notification.is_read = True
    notification.save(update_fields=["is_read"])

    return redirect("notification_list")


@login_required
def mark_all_notifications_read(request):
    Notification.objects.filter(
        recipient=request.user,
        is_read=False,
    ).update(is_read=True)

    return redirect("notification_list")