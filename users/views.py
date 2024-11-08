
# Create your views here
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created!')
            return redirect('login')  # Redirect to the login page or homepage
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

