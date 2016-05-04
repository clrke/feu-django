from django.shortcuts import render
from tasks.models import Task
from django.core import serializers

def all(request):
    tasks = [t.serialize() for t in Task.objects.all()]
    return render(request, 'index.html', {'tasks': tasks})


def one(request, id):
    return render(request, 'show.html',
        {'task': Task.objects.get(pk=id).serialize()}
    )

