from django.shortcuts import render, redirect
from blog.forms import CustomUserCreationForm, CustomLoginForm, BlogPostForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from .models import BlogPost, CustomUser
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.views.generic import DeleteView


# Create your views here.

def blog(request):
    return render(request, 'blog.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def allposts(request):
    return render(request, 'all-posts.html')

def getstarted(request):
    return render(request, 'get-started.html')

def login(request):
    return render(request, 'login.html')

def lifestyle(request):
    return render(request, 'lifestyle.html') 

def tech(request):
    return render(request, 'tech.html')  

def travel(request):
    return render(request, 'travel.html')

def newblog(request):
    return render(request, 'newblog.html')

def createview(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user  # Set the logged-in user as the author
            blog.save()
            return redirect('allposts')
    else:
        form = BlogPostForm()
    return render(request, 'newblog.html', {"form": form})

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful')
            return redirect('login')
        else:
            messages.error(request, 'Registration Invalid.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'authentication/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('blog')  # Update 'blog' with your desired redirect URL

class CustomLogoutView(LogoutView):
    template_name = 'authentication/logout.html'
    next_page = reverse_lazy('login')

@login_required
def admin_register_user(request):
    if request.user.role != 'admin':
        messages.error(request, "Access Denied: Admin privileges required")
        return redirect('dashboard')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f"User {user.username} created successfully")
            return redirect('user_list')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'admin/register_user.html', {'form': form})

@login_required
def user_list(request):
    if request.user.role != 'admin':
        messages.error(request, "Access Denied: Admin privileges required")
        return redirect('dashboard')

    users = CustomUser.objects.all()
    return render(request, 'admin/user_list.html', {'users': users})

@login_required
def edit_user(request, user_id):
    if request.user.role != 'admin':
        messages.error(request, "Access Denied: Admin privileges required")
        return redirect('dashboard')

    user = CustomUser.objects.get(pk=user_id)
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "User updated successfully")
            return redirect('user_list')
    else:
        form = CustomUserChangeForm(instance=user)
    
    return render(request, 'admin/edit_user.html', {'form': form})

from django.shortcuts import get_object_or_404

def detailview(request, pk):
    # Replace BlogPost with your model name
    blog_post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'detailview.html', {'blog_post': blog_post})
class BlogPostUpdateView(UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blog/blogpost_form.html'
    success_url = '/success-url/'  # Redirect after successful update
class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blog/blogpost_confirm_delete.html'
    success_url = '/blog/'