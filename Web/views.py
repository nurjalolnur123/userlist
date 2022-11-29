from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def home(request):
    try:
        code = request.build_absolute_uri().split("?")[1]
    except:
        code = None

    context = {
        "peoples": Peoples.objects.all(),
        'code': code,
    }
    return render(request, 'index.html', context)

def add_people(request):
    if request.method == 'POST':
        users = Peoples.objects.all()

        for i in users:
            if request.POST['name'].lower() == i.name.lower():
                return redirect('/?name')

        u = Peoples.objects.create(
            name = request.POST['name'],
            age = request.POST['age'],
        )
    return redirect('/?success')