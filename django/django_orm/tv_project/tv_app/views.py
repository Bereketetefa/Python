from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

def index(request):
	context = {
	    'all_dates': Show.objects.all() 
	}
	return render(request,"allshows.html",context)

def createShowPage(request):
	return render(request, "create.html")

def createShow(request):
	print(request.POST)
	responsefromValidator =  Show.objects.fanValidator(request.POST)
	if len(responsefromValidator) > 0:
		for key, value in responsefromValidator.items():
			messages.error(request, value)
		return redirect('/createShowPage')
	else: 
		newshow = Show.objects.create(title = request.POST['name'], Network = request.POST['network'], Release= request.POST['release'], desc = request.POST['description'])
	print(newshow)
	return redirect(f"/shows/{newshow.id}")

def showInfo(request, show_id):
	showToshow = Show.objects.get(id= show_id)
	print(showToshow)
	context = {
		'tvshow': showToshow
	}
	return render(request, 'Read.html', context)

def editShow(request, show_id):
	showToEdit = Show.objects.get(id= show_id)
	print(showToEdit)
	context = {
		'editshow': showToEdit
	}
	return render(request, 'update.html', context)

def updateShow(request, show_id):
	responseEditValidator =  Show.objects.editValidator(request.POST)
	if len(responseEditValidator) > 0:
		for key, value in responseEditValidator.items():
			messages.error(request, value)
		return redirect(f'/shows/{show_id}/edit')	
	else:
		editShow = Show.objects.get(id= show_id)
		editShow.title = request.POST['nombre']
		editShow.Network = request.POST['net']
		editShow.Release = request.POST['rel']
		editShow.desc = request.POST['description']
		editShow.save()
	print(request.POST)
	return redirect(f'/shows/{show_id}')

def delete(request, show_id):
	showtodelete = Show.objects.get(id= show_id)
	showtodelete.delete()
	return redirect('/shows')

	# context = {
	# 	'showToshow': Course.objects.get(id= show_id)
	# }
	# return render(request,'allshows.html', context)

# def process_edit(request, allshows_id):
# 	showToEdit = show.objects.get(id= allshows_id)
# 	context = {
# 		'editshow': showToEdit
# 	}

# 	return render(request, 'update.html')
