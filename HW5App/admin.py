from django.contrib import admin

# Register your models here.
from HW5App.models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    def has_view_permission(self, request, obj=None):
        return True


admin.site.register(BlogPost, BlogPostAdmin)