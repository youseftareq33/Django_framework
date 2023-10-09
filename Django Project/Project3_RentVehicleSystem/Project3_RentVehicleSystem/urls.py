from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect

# Signup view
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vehicles/', include('vehicles.urls')),
    
    # Login Template
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    
    # Logout Template
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    
    # Signup Template
    path('signup/', signup, name='signup'),
]


