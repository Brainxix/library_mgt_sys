from django.urls import path
from . import views
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import RedirectView

urlpatterns = [
    path("", RedirectView.as_view(url="/login/", permanent=False)),
    
    path("register/", views.register_view, name="register"),
    
    path("login/", views.login_view, name="login"),
    
    path("logout/", views.logout_view, name="logout"),
    
    path("profile/", views.profile_view, name="profile"),
    
]