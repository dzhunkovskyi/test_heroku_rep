from django.shortcuts import render
from .models import Post, Comments
from .forms import CommentForm

from django.http import HttpResponse
from django.shortcuts import render, redirect, render_to_response
from django.contrib import auth
from django.contrib.auth import login, authenticate
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.template.context_processors import csrf
from django.core.paginator import Paginator
# Create your views here.


def main(request, page_number=1):
	print('MAIN')
	context = {}
	posts_list = Post.objects.all().order_by('-post_date')
	current_page = Paginator(posts_list, 2)
	username = request.user.username
	if username:
		context['username'] = username		
	context['list_of_posts'] = current_page.page(page_number)
	return render(request, 'posts/main.html', context)


def post(request, post_id, page_number=1):
	context = {}
	post = Post.objects.get(id=post_id) # identify which manager you want
	comments = post.comments_set.all()
	comment_form = CommentForm()
	username = request.user.username
	post = Post.objects.get(id=post_id)
	comments_list = Comments.objects.all().order_by('-post_date')
	current_page = Paginator(comments_list, 2)
	context['form'] = comment_form
	context['post'] = post
	context['username'] = username
	context['comments'] = current_page.page(page_number)
	return render(request, 'posts/post_page.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            message = render_to_string('posts/acc_active_email.html', {
                'user':user, 
                'domain':current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            mail_subject = 'Activate your blog account.'
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    
    else:
        form = SignupForm()
    
    return render(request, 'posts/signup.html', {'form': form})


def activate(request, uidb64, token):
	try:
		uid = force_text(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
	except(TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None
	if user is not None and account_activation_token.check_token(user, token):
		user.is_active = True
		user.save()
		login(request, user)
		# return redirect('home')
		# return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
		return redirect('/')
	else:
		return HttpResponse('Activation link is invalid!')


def login_func(request):
	args = {}
	args.update(csrf(request))
	if request.POST:
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			return redirect('/')
		else:
			args['login_error'] = 'Log in error'
			return render_to_response('posts/login.html', args)
	else:
		return render(request, 'posts/login.html', args)


def logout(request):
    auth.logout(request)
    return redirect('/')


def addlike(request, post_id):
	print('ADDLIKE!')
	username = request.user.username
	print('username=', username)
	post = Post.objects.get(id=post_id)
	# user = User.objects.get(username=username)
	# if username and user not in technik.users_liked.all():
	if username not in post.return_list_of_user():
		print('+')
		print('post.return_list_of_user()', post.return_list_of_user())
		print('post_rate=', post.post_likes)
		post.post_likes += 1
		print('post_rate=', post.post_likes)
		post.add_user(username)
		post.save()
	else:
		print('-')
		print('post.return_list_of_user() = ', post.return_list_of_user())
		print('post_rate=', post.post_likes)
		post.post_likes -= 1
		print('post_rate=', post.post_likes)
		post.delete_user(username)
		post.save()
	return redirect('/')


def addcomment(request, post_id):
	args = {}
	username = request.user.username
	args.update(csrf(request))
	if request.POST:
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.name_of_user = username
			comment.comment_post = Post.objects.get(id=post_id)
			comment.comments_post_id = post_id
			print('COMMENT_POST = ', comment.comment_post)
			form.save()
			request.session.set_expiry(60)
			request.session['bla'] = True
		return redirect('/post/%s/1/' % post_id)