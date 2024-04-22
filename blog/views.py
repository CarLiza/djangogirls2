from django.shortcuts import render # type: ignore
from django.utils import timezone # type: ignore
from .models import Post
# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts}) # type: ignore