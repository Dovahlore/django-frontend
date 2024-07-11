from django.shortcuts import render, HttpResponse, redirect
from django import forms
from django.http import JsonResponse
import app.models as models
from django.core.paginator import Paginator
from django import forms
from django.db.models import Q


class filter_tasks_form(forms.ModelForm):
    class Meta:
        model = models.task_list
        fields = ['status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['status'].required = False
        self.fields['status'].initial = ""
        self.fields['status'].widget.attrs.update(
            {'style': 'width:200px;color:blue;border: 2px solid #000; margin-right:25px;', 'class': ' form-control'})


def task(request):
    tasks = models.task_list.objects.select_related('task').all()  # 假设你的模型名称是TaskList
    form = filter_tasks_form()
    filters = Q()

    if request.method == 'POST':
        form = filter_tasks_form(request.POST)
        filters = Q()
        if form.is_valid():
            page_number = 1
            if form.cleaned_data.get('status'):
                status = form.cleaned_data['status']
                filters &= Q(status=status)

            tasks = tasks.filter(filters).distinct()
            message = "共%s条结果" % (len(tasks))
            paginator = Paginator(tasks, 20)
            tasks = paginator.get_page(page_number)

            return render(request, "tasks.html", {
                "tasks": tasks,
                'paginator': paginator,
                "form": form,
                "messages": message,
            })
    page_number = request.GET.get('page')
    status = request.GET.get('status')
    if status:

        filters &= Q(status=status)

        tasks = tasks.filter(filters).distinct()
        message = "共%s条结果" % (len(tasks))
        initial_data = {
            'status': status
        }
        form = filter_tasks_form(initial=initial_data)
    else:
        message = "共%s条结果" % (len(tasks))
    paginator = Paginator(tasks, 20)

    tasks = paginator.get_page(page_number)

    return render(request, "tasks.html", {
        "tasks": tasks,
        'paginator': paginator,
        "form": form,
        "messages": message,

    })


def get_meta_tasks(request):
    task_id = request.GET.get('task_id')
    meta_tasks_list = models.meta_task_list.objects.select_related('meta_task', 'server').filter(
        belong_to_task_id=task_id)

    return JsonResponse({'meta_tasks': [
        {'id': meta_task.id, 'core': meta_task.meta_task.core, 'GPU': meta_task.meta_task.GPU,
         'name': meta_task.meta_task.meta_task_name, 'server': meta_task.server.Ip_mapping} for meta_task
        in meta_tasks_list]
    })
