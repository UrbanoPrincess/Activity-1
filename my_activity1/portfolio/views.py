from django.shortcuts import render
def index(request): 
    return render(request, "pages/portfolio.html")
def about(request):
    return render(request, 'pages/about.html')  # Ensure correct path to template

def projects(request):  # Use plural "projects" for projects page
    return render(request, 'pages/projects.html')

def activity2(request):  # Separate function for activity2 page
    return render(request, 'pages/activity2.html')

def dashboard(request):  # Separate function for dashboard page
    return render(request, 'pages/dashboard.html')
# Create your views here.
