from django.urls import path, include
from todo_app.views import index, TagListView, TaskCreateView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('home/', index, name='index'),
    path('tags/', TagListView.as_view(), name='tags'),
    path('task/create', TaskCreateView.as_view(), name='task_create'),
    path('task/<int:pk>/update', TaskUpdateView.as_view(), name='task_update'),
    path('task/<int:pk>/delete', TaskDeleteView.as_view(), name='task_delete'),

]

app_name = "todo_app"