from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="home"),
	path('favorites', views.add_stock, name="add_stock"),
	path('delete/<stock_id>', views.delete, name="delete"),
	path('news', views.news, name="news"),
	path('about', views.about, name='about')
]