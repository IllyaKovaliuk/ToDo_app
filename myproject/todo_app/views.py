from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpRequest, Http404
from django.urls import reverse_lazy
from django.views import generic

from todo_app.models import Task, Tag


def index(request: HttpRequest) -> HttpResponse:
    num_tasks = Task.objects.prefetch_related('tags').all()
    context = {
        'num_tasks': num_tasks,
    }
    return render(request, 'todo_app/home.html', context=context)


class TagListView(generic.ListView):
    model = Tag
    context_object_name = 'tags'
    template_name = "todo_app/tag_list.html"


class TaskCreateView(generic.CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('todo_app:index')
    template_name = 'todo_app/task_create.html'


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('todo_app:index')
    template_name = 'todo_app/task_update.html'

class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy('todo_app:index')
    template_name = 'todo_app/task_delete.html'


def TaskSwithcher(request: HttpRequest, task_id: int) -> HttpResponse:
    task = get_object_or_404(Task, pk=task_id)
    task.done_not_done = not task.done_not_done
    task.save()
    return redirect('todo_app:index')


class TagCreateView(generic.CreateView):
    model = Tag
    fields = '__all__'
    success_url = reverse_lazy('todo_app:tags')
    template_name = ('todo_app/tag_create.html')

class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = '__all__'
    success_url = reverse_lazy('todo_app:tags')
    template_name = ('todo_app/tag_update.html')


class TagDeleteView(generic.DeleteView):
    model = Tag
    fields = '__all__'
    success_url = reverse_lazy('todo_app:tags')
    template_name = ('todo_app/tag_delete.html')