from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),    
    path('createBook', views.createBook),
    path('Books/<BooksId>', views.showBook)

]
