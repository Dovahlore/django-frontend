from django.shortcuts import render, HttpResponse, redirect
from django import forms
from django.http import JsonResponse
import app.models as models


def task(request):
    tasks = models.task_list.objects.select_related('task').all()
    return render(request, "tasks.html", {"tasks": tasks})


def get_meta_tasks(request):
    task_id = request.GET.get('task_id')
    meta_tasks_list = models.meta_task_list.objects.select_related('meta_task', 'server').filter(
        belong_to_task_id=task_id)

    return JsonResponse({'meta_tasks': [
        {'id': meta_task.id, 'core': meta_task.meta_task.core, 'GPU': meta_task.meta_task.GPU,
         'name': meta_task.meta_task.meta_task_name, 'server': meta_task.server.Ip_mapping} for meta_task
        in meta_tasks_list]
                         })
