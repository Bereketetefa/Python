from django.urls import path
from . import views 

urlpatterns = [ 
    path('', views.index),
    path('new', views.new),
    path('create', views.index),
    path('show/<str:data_from_route>',views.show),
    path('number/edit<str:data_from_route2',views.number),
    path('', views.destroy)
]
# from django.urls import path
# from . import views
# urlpatterns = [
#     path('', views.index),	   
# ]