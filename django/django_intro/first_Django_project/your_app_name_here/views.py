from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    print(request)
    return HttpResponse('placeholder to later display new')

def create(request):
    return redirect('/')

def show(request,data_from_route):
    print(request)
    print(data_from_route)
    return HttpResponse(f"placeholder to later display what i type{data_from_route}")

def number(request,data_from_route2):
    print(request)
    print(data_from_route2)
    return HttpResponse(f"placeholder to edit blog {number}")

def destroy(request,data_from_route3):
    
    return redirect('/')