from django.shortcuts import render
from django.http import HttpResponse
from .models import Animal 
from django.core import serializers
# Create your views here.

def create_animal(request):
    name = request.GET.get('name')
    age = request.GET.get('age')
    kind = request.GET.get('kind')
    image_url = request.GET.get('image_url')
    breed = request.GET.get('breed')
    description = request.GET.get('description')


    animal = Animal(name=name, age=age, kind=kind, image_url=image_url, breed=breed, description=description)
    animal.save()
    return HttpResponse('CREATED!!!!')

    # http://127.0.0.1:8000/animals/create/?name='shushi'&age=27&breed='some_breed&kind='Dog'&description='some'&imgage_url=https://img.washingtonpost.com/wp-apps/imrs.php?src=https://img.washingtonpost.com/rf/image_960w/2010-2019/WashingtonPost/2017/02/07/Editorial-Opinion/Images/Merlin_18620419.jpg&w=480

def edit_animal(request, animal_id):
    animal = Animal.objects.get(pk=animal_id)
    name = request.GET.get('name')
    animal.name = name
    
def delete_animal(request, animal_id):
    try:
        animal = Animal.objects.get(pk=animal_id)
        animal.delete()
        return HttpResponse('DELETED!!!!!!')
    except Animal.DoesNotExist:
        return HttpResponse('NOT DELETED!')

def serialized_data(data):
    try:
        return serializers.serialize('json', data)
    except:
        return serializers.serialize('json', [data])

def get_all_animals(request):
    name = request.GET.get('name')
    if name:
        animal = Animal.objects.all().filter(name=name)
        return HttpResponse(serialized_data(animal))
    animals = Animal.objects.all()
    return HttpResponse(serialized_data(animals))

def get_animal(request, animal_id):
    animal = Animal.objects.get(pk=animal_id)
    return HttpResponse(serialized_data(animal))

def get_all_dogs(request):
    dogs = Animal.objects.all().filter(kind='D')
    return HttpResponse(serialized_data(dogs))

def get_all_cats(request):
    cats = Animal.objects.all().filter(kind='C')
    return HttpResponse(serialized_data(cats))

def order_animals(request):
    animals = Animal.objects.all().order_by('age')
    return HttpResponse(serialized_data(animals))