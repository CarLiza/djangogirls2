from django.contrib import admin  # type: ignore
from .models import Post, Comment

# Register your models here.
admin.site.register(Post)

admin.site.register(Comment)