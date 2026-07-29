"""
URL configuration for project_config project.

The `urlpatterns` list routes URLs to views.
"""

from django.contrib import admin
from django.urls import path,include 

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path("", include("core.urls")),
    
    path("accounts/", include("accounts.urls")),
    
    path("dashboard/", include("dashboard.urls")),
    
    path("books/", include("books.urls")),
    
    path("members/", include("members.urls")),
    

]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)