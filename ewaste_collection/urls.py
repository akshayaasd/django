from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('show_ewaste/', views.show_ewaste, name='show_ewaste'),
    path('success/', views.ewaste_collection_success, name='ewaste_collection_success')
]
