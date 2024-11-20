from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms
from .models import BlogPost
from tinymce.widgets import TinyMCE
from django.contrib.auth.forms import AuthenticationForm
from blog import views
from users.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """
    Form for creating new users
    """
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
        
    def clean_email(self):
        """
        Validate unique email
        """
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")
        return email

class CustomUserChangeForm(UserChangeForm):
    """
    Form for updating user information
    """
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'is_active')
        

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        })
    )

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title',  'content', 
        ]


class BlogPostForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'cover_image', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'tags': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter tags separated by commas'}),
        }

# @login_required
def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            messages.success(request, 'Blog post created successfully!')
            return redirect('blog_detail', slug=blog_post.slug)
    else:
        form = BlogPostForm()
    
    return render(request, 'blog/create_post.html', {'form': form})