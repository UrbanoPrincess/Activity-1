from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

from portfolio import views  # Import views correctly

urlpatterns = [
    path('admin/', admin.site.urls),
    path('portfolio/', include(('portfolio.urls', 'portfolio'), namespace="portfolio")),  # Fix namespace issue
    path('', lambda request: redirect('portfolio:index'), name='home'),  # Redirect to portfolio.index

    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),  # Fix: Use views.projects (plural)
    path('activity2/', views.activity2, name='activity2'),  # Fix: Use views.activity2 (if it exists)
    path('dashboard/', views.dashboard, name='dashboard'),
    path('reports/', views.reports, name='reports'),  # Add reports path
    path('setting/', views.setting, name='setting'),  # Add setting path
]
