from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('register', views.registerUser),
    path('home', views.home),
    path('logout', views.logout),
    path('login', views.login),
    path('quotes', views.quotes),
    path('quotes/<show_id>/edit', views.updatePost),
    path('quotes/<show_id>/delete', views.delete),
    path('contquote', views.createQuote),
    path('addfavorite', views.favorites),
    path('delfavorite', views.delfavorites),
    path('users/<show_id>', views.editShow),
    path('quotes/<show_id>', views.edit)
]