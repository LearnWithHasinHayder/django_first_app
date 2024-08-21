from django.shortcuts import render
from .models import Task 

# Create your views here.

def task_list(request):
    # tasks = Task.objects.filter(completed=True)
    tasks = Task.objects.all()
    completed = request.GET.get("completed")
    if completed == '1':
        tasks = tasks.filter(completed=True)
    elif completed == '0':
        tasks = tasks.filter(completed=False)
    return render(request, 'task_list.html', {"tasks":tasks})

def task_details(request, pk):
    task = Task.objects.get(pk=pk)
    return render(request, 'task_detail.html', {"task":task})