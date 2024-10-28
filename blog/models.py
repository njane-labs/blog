from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User  # To link with User accounts
from django.utils.timezone import now

class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to a user
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)  # Optional image
    tags = models.CharField(max_length=100, help_text="Comma-separated tags")  # e.g., 'tech, lifestyle'
    created_at = models.DateTimeField(default=now, editable=False)  # Creation timestamp
    updated_at = models.DateTimeField(auto_now=True)  # Update timestamp

    def __str__(self):
        return self.title  # Displays title in admin and queries
