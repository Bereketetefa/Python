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
	newuser = User.objects.create(firstname = request.POST['firstname'], lastname = request.POST['lastname'], email = request.POST['email'], password = hash1)
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
	print(request.POST)
	loginValidator = User.objects.loginValidator(request.POST)
	print(error_validation)
	if len(error_validation)>0:
		for key, value in error_validation.items():
			messages.error(request, value)
		return redirect('/')
	
	User = User.objects.get(email = request.POST['email'])
	request.session['loggedinId'] = User.id
	return redirect ('/home')


def logout(request):
	request.session.clear()
	return redirect('/')


