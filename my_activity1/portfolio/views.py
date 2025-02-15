from django.shortcuts import render
def index(request): 
    return render(request, "pages/portfolio.html") 

def about(request):
    return render(request, 'pages/about.html')  # Ensure correct path to template

def project(request):
    return render(request, 'pages/projects.html')
# Create your views here.
