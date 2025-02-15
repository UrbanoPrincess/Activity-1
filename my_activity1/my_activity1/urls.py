from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

from portfolio import views  # Import redirect function

urlpatterns = [
    path('admin/', admin.site.urls),
    path('portfolio/', include('portfolio.urls', namespace="portfolio")),
    path('', lambda request: redirect('portfolio:index'), name='home'),  # Redirect to portfolio.index
      path('about/', views.about, name='about'),
    path('projects/', views.project, name='projects'),
]
