# crm_project/urls.py

from django.contrib import admin
from django.urls import path, include
from crm import views  # Import views from the crm app
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
urlpatterns = [
    path('admin/', admin.site.urls),
    path('crm/', include('crm.urls')),  # Include crm app's urls
    path('', views.home, name='home'),  # Define the root path and link it to a 'home' view
]



# Home page view
def home(request):
    return render(request, 'home.html')

# Whiteboard view
def whiteboard(request):
    return render(request, 'whiteboard.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # 👈 Adds homepage here!
    path('whiteboard/', whiteboard, name='whiteboard'),
]


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/dashboard/')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_login, name='login'),  # 👈 Login at homepage
    path('dashboard/', dashboard, name='dashboard'),
]

