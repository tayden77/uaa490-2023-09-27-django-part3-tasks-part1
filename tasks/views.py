from django.shortcuts import render
from .forms import NewTaskForm

tasks = ['eat', 'sleep', 'pray'
]

def index(request):
    return render(request, 'tasks/index.html', {
        'tasks': tasks
    })

def add(request):
    return render(request, "tasks/add.html")

def add(request):
    return render(request, "tasks/add.html", {"form": NewTaskForm()})