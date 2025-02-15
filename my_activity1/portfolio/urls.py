from django.urls import path
from .views import index

app_name = "portfolio"  # Namespace for the app

urlpatterns = [
    path('', index, name='index'),  # Define the URL for the portfolio page
]
