from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.


def home(request):
    return render(request, 'index.html', {'tasks': Task.objects.all()})


def task_info(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'taskInfo.html', {'task':task})


