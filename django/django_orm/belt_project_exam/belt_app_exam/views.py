from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

def index(request):
	return render(request,"index.html")


def registerUser(request):
	print(request.POST)
	validationErrors = User.objects.registrationValidator(request.POST)
	if len(validationErrors)> 0:
		for key, value in validationErrors.items():
			messages.error(request, value)
		return redirect('/')
	hash1 = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
	newuser = User.objects.create(email = request.POST['email'], password = hash1)
	request.session['loggedinId'] = newuser.id
	return redirect('/home')

def home(request):
	if 'loggedinId' not in request.session:
		return redirect('/')
	context = {
		'loggedinUser': User.objects.get(id = request.session['loggedinId'])
	}
	return render(request, 'home.html', context) 


def login(request):
	print(User)
	loginValidator = User.objects.loginValidator(request.POST)
	print(loginValidator)
	if len(loginValidator)>0:
		for key, value in loginValidator.items():
			messages.error(request, value)
		return redirect('/')
	# print(User.objects.get(id=2))
	# print(User.objects.get(email = request.POST['email']))
	U = User.objects.get(email = request.POST['email'])
	request.session['loggedinId'] = U.id
	return redirect ('/quotes')


def quotes(request):
	user_id = request.session['loggedinId']
	favorites = Favorite.objects.filter(user_id__exact = user_id)
	favmap = {}
	for favorite in favorites:
		favmap[favorite.post.id] = True

	posts = Post.objects.all()
	all_posts = []
	for post in posts:
		if post.id not in favmap: 
			all_posts.append(post)

	context = {
		'loggedinUser': User.objects.get(id = user_id),
		'all_posts': all_posts, 
		'favorites': favorites
	}
	print(context)
	return render(request, 'post.html',context)

def showquotes(request):
	return redirect('/quotes')

def createQuote(request):
	quoteValidator = Post.objects.quoteValidator(request.POST)
	print(quoteValidator)
	if len(quoteValidator)>0:
		for key, value in quoteValidator.items():
			messages.error(request, value)
		return redirect('/quotes')	
	U = User.objects.get(id = request.session['loggedinId'])
	Post.objects.create(user = U, post = request.POST['quote'] ,quoted_by = request.POST['quotedby'])
	return redirect ('/quotes')

def favorites(request):
	U = User.objects.get(id = request.session['loggedinId'])
	P = Post.objects.get(id = request.POST['post_id'])
	Favorite.objects.create(user = U, post = P)
	return redirect ('/quotes')

def delfavorites(request):
	F = Favorite.objects.get(id = request.POST['post_id'])
	F.delete()
	return redirect ('/quotes')
	
def editShow(request, show_id):
	P = Post.objects.filter(user_id__exact = show_id)	
	context = {
		'all_posts': P,
		'User': User.objects.get(id = show_id),
		'count': len(P)
	}
	return render(request, 'update.html', context)

def edit(request, show_id):
	P = Post.objects.get(id = show_id)	
	context = {
		'post': P,
	}
	return render(request, 'edit.html', context)

def updatePost(request, show_id):
	if "cancel" in request.POST : 
		return redirect('/quotes')

	responseEditValidator =  Post.objects.quoteValidator(request.POST)
	if len(responseEditValidator) > 0:
		for key, value in responseEditValidator.items():
			messages.error(request, value)
		return redirect(f'/quotes/{show_id}/edit')	
	else:
		editpost = Post.objects.get(id= show_id)
		editpost.post = request.POST['quote']
		editpost.quoted_by = request.POST['quotedby']
		editpost.save()
	print(request.POST)
	return redirect('/quotes')

def delete(request, show_id):
	showtodelete = Post.objects.get(id= show_id)
	showtodelete.delete()
	return redirect('/quotes')

def logout(request):
	request.session.clear()
	return redirect('/')