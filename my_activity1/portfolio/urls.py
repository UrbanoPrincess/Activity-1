from django.urls import path

from portfolio import views
from .views import index

app_name = "portfolio"  # Namespace for the app

urlpatterns = [
    path('', index, name='index'),  # Define the URL for the portfolio page
    path('about/', views.about, name='about'),
    path('projects/', views.project, name='projects'),
]
