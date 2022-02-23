from django.shortcuts import render

import random

# Create your views here.


def about(request):
    return render(request, 'generator/About.html')


def home(request):
    return render(request, 'generator/Home.html')


def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    generated_password = ''
    
    length = int(request.GET.get('length'))     # Tamagno de la cadeja.    
    uppercase = request.GET.get('uppercase')    # Si tiene mayusculas
    special = request.GET.get('special')        # Si tienes characteres especiales.
    numbers = request.GET.get('numbers')        # Si tiene numeros.

    if uppercase:
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    
    if special:
        characters.extend(list('!"#$%&()*+,-./:;<=>?@[\]^_`{|}~'))
        
    
    if numbers:
        characters.extend(list('0123456789'))

    for x in range(length):
        generated_password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': generated_password})
