#accounts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('index/', views.IndexView.as_view(), name='index'),  # Define the URL pattern for the index view
    # Add other URL patterns for account-related views if needed
]
