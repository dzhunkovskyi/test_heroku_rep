from django.shortcuts import render
from .models import Post
# Create your views here.

def main(request):
	posts_list = Post.objects.all()
	context = {'list_of_posts': posts_list}
	return render(request, 'posts/main.html', context)