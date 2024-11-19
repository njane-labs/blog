
from django.contrib import admin
from django.utils.html import format_html
from .models import BlogPost
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # Customize as needed, e.g., add fields to list display or filter options
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')


def make_published(modeladmin, request, queryset):
    queryset.update(status='published')

make_published.short_description = 'Mark selected posts as published'

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author','created_at', 'updated_at')
    list_filter = ('created_at', 'author',)
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    actions = [make_published]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)

    def status_icon(self, obj):
        if obj.status == 'published':
            return format_html('<i class="fa fa-check-circle" style="color: green;"></i>')
        return format_html('<i class="fa fa-times-circle" style="color: red;"></i>')
    status_icon.short_description = 'Status'

admin.site.register(BlogPost, BlogPostAdmin)
