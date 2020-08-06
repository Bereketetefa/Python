from django.urls import path
from . import views

urlpatterns = [
    path('', include('time_display_app.urls')),
]



