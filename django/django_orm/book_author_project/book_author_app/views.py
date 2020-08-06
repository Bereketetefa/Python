from django.shortcuts import render, redirect
from .models import *

def index(request):
	context = {
		'allbooks': Book.objects.all()
	}
	return render(request,"index.html", context)

def createBook(request):
	print(request.POST)
	# Book.objects.create(title = request.POST['b_Name'], desc = request.POST['desc'])
	Book.objects.create(title = request.POST['b_Name'], desc = request.POST['desc'])
	
	return redirect("/")

def showBook(request, bookId):
	return render(request, 'index2.html')