from multiprocessing import context
from django.shortcuts import render
from computerapp.models import Personnel, Machine

def index(request):
    machines = Machine.objects.all()
    personnels = Personnel.objects.all()

    context = {
        'machines': machines,
        'personnels': personnels,
    }

    return render(request, 'template/index.html',context=context)

# Create your views here.

def login(request):
    machines = Machine.objects.all()
    personnels = Personnel.objects.all()

    context = {
        'machines': machines,
        'personnels': personnels,
    }

    return render(request, 'template/login.html',context=context)


def machine_list(request):
    machines = Machine.objects.all()
    personnels = Personnel.objects.all()

    context = {
        'machines': machines,
        'personnels': personnels,
    }

    return render(request, 'template/machines.html',context=context)

def utilisateurs(request):
    machines = Machine.objects.all()
    personnels = Personnel.objects.all()

    context = {
        'machines': machines,
        'personnels': personnels,
    }

    return render(request, 'template/utilisateurs.html',context=context)
