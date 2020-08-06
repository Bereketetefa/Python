from django.urls import path     
from . import views
urlpatterns = [
	path('shows', views.index), 
	path('createShowPage',views.createShowPage),
	path('createShow',views.createShow),
	path('shows/<show_id>', views.showInfo),
	path('shows/<show_id>/edit', views.editShow),
	path('shows/<show_id>/update', views.updateShow),
	path('shows/<show_id>/destroy', views.delete)
]
	# path('Books/<BooksId>', views.showBook)
	# path('/shows/<show_id>',views.edit_show),
	# path('shows/<allshows_id>',views.process_edit)