from django.shortcuts import render
import random


# Create your views here.

def home(request):
    return render(request, 'generator/index.html')


def generate(request):
    letters = list('abcdefghijklmnopqrstuvwxyz')
    password = ''
    length = int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        letters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        letters.extend(list('!"#$%&/()=?»«)\'\"@£§€{[]}*\\+.,<>'))

    if request.GET.get('numbers'):
        letters.extend(list('0123456789'))

    for letter in range(length):
        password += random.choice(letters)

    return render(request, 'generator/generate.html', {'password': password})


def about(request):
    return render(request, 'generator/about.html')

