from django.urls import path
from portfolio import views  # Ensure correct import
from .views import index

app_name = "portfolio"  # Namespace for the app

urlpatterns = [  # ✅ Fix: Changed from 'uurlpatterns' to 'urlpatterns'
    path('', index, name='index'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('activity2/', views.activity2, name='activity2'),
    path('dashboard/', views.dashboard, name='dashboard'),  # Add dashboard path
]
