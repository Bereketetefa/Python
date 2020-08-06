from django.shortcuts import render, HttpResponse
# from .models import books

def index(request):
    return render(request,"index.html")