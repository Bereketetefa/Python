from django.urls import path, include 

urlpatterns = [
    path('', include('helloApp.urls')),
]