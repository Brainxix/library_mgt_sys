"""
URL configuration for project_config project.

The `urlpatterns` list routes URLs to views.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin
    path("admin/", admin.site.urls),

    # Django Authentication
    path("accounts/", include("django.contrib.auth.urls")),

    # Project Apps
    path("", include("dashboard.urls")),
    path("books/", include("books.urls")),
    path("members/", include("members.urls")),
    path("transactions/", include("transactions.urls")),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)