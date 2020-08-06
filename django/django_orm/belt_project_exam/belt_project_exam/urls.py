from django.urls import path, include 

urlpatterns = [
    path('', include('belt_app_exam.urls')),
]