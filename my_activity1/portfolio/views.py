from django.shortcuts import render
def index(request): 
    return render(request, "pages/portfolio.html") 

# Create your views here.
