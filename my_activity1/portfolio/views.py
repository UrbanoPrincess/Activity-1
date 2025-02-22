from django.shortcuts import render

def index(request): 
    return render(request, "pages/portfolio.html")

def about(request):
    return render(request, 'pages/about.html')  

def projects(request):  
    return render(request, 'pages/projects.html')

def activity2(request):  
    return render(request, 'pages/activity2.html')

def reports(request):  
    return render(request, 'pages/reports.html')

def setting(request):  
    return render(request, 'pages/setting.html')

def dashboard(request):  
    data = [
        {"title": "Users", "count": 150},
        {"title": "Orders", "count": 320},
        {"title": "Revenue", "count": "12,450"},
    ]
    return render(request, 'pages/dashboard.html', {'data': data})  # Pass data to template
