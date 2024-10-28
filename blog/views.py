from django.shortcuts import render

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

