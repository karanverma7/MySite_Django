from django.shortcuts import render
from .models import List
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages


def home(request):
    if request.POST:
        task = List(task=request.POST['item'])
        task.save()
        task_list = List.objects.all()
        messages.success(request, 'Task has been added to the List')
        return render(request, 'ToDoList/main.html', {'TaskList': task_list})
    else:
        task_list = List.objects.all()
        return render(request, 'ToDoList/main.html', {'TaskList': task_list})


def delete(request, task_id):
    task = List.objects.get(pk=task_id)
    task.delete()
    messages.success(request, 'Task has been deleted from the List')
    return HttpResponseRedirect(reverse('ToDoList:home'))


def cross(request, task_id):
    task = List.objects.get(pk=task_id)
    task.completed = True
    task.save()
    return HttpResponseRedirect(reverse('ToDoList:home'))


def uncross(request, task_id):
    task = List.objects.get(pk=task_id)
    task.completed = False
    task.save()
    return HttpResponseRedirect(reverse('ToDoList:home'))