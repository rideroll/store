from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path('^all/$', views.get_all_animals, name='all'),
    path('all/<int:animal_id>/', views.get_animal, name='animal'),
    path('all/dogs/', views.get_all_dogs, name='all_dogs'),
    path('all/cats/', views.get_all_cats, name='all_cats'),
    path('all/ordered/', views.order_animals, name='all_ordered'),
    path('create/', views.create_animal, name='create'),
    re_path('^edit/<int:animal_id>/$', views.edit_animal, name='edit'),
    re_path('delete/(?P<animal_id>\d+)/', views.delete_animal, name='delete'), 
]