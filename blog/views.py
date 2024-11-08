from django.shortcuts import render
from blog.forms import CustomUserCreationForm, CustomLoginForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView


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
    return render(request,'login.html')


def lifestyle(request):
    return render(request, 'lifestyle.html') 


def tech(request):
    return render(request, 'tech.html')  


def travel(request):
    return render(request, 'travel.html')


def newblog(request):
    return render(request, 'newblog.html')


from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

def register_view(request):
    if request.method == 'POSTS':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            login(request)
            message.success(request, 'Registration successful')
            return redirect('home')
        else:
            messages.error(request, 'Registrtion Invalid.')
    else:
        form =  CustomUserCreationForm()
    return render(request, 'get-started.html', {'form': form})
    
    




# class SignUpView(CreateView):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'get-started.html'



class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'authentication/login.html'
    success_url = reverse_lazy('home')  # Change 'home' to your desired redirect URL
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return self.success_url

class CustomLogoutView(LogoutView):
    template_name = 'authentication/logout.html'
    next_page = reverse_lazy('login')
