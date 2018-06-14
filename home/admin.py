from django.contrib import admin
from .models import Post, Apply


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("id",)}

@admin.register(Apply)
class ApplyAdmin(admin.ModelAdmin):
    list_display = ('post', 'applicant','created')

