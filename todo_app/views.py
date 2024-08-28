from django.shortcuts import render, redirect
from .models import Task
from django.http import HttpResponse
from .forms import TaskForm

# Create your views here.


def task_list(request):
    # tasks = Task.objects.filter(completed=True)
    tasks = Task.objects.all()
    completed = request.GET.get("completed")
    if completed == "1":
        tasks = tasks.filter(completed=True)
    elif completed == "0":
        tasks = tasks.filter(completed=False)
    return render(request, "task_list.html", {"tasks": tasks})


def task_details(request, pk):
    task = Task.objects.get(pk=pk)
    return render(request, "task_detail.html", {"task": task})


def add_task(request):
    _title = "Let's have dinner together X"
    _description = "Dinner invitation at Chefs Table X"
    _completed = False
    _due_date = "2024-08-28"
    task = Task(
        title=_title, description=_description, completed=_completed, due_date=_due_date
    )
    task.save()
    # return HttpResponse("Adding Task");
    return redirect("task_list")

    # CRUD


def delete_task(request, pk):
    try:
        task = Task.objects.get(pk=pk)
        task.delete()
        return redirect("task_list")
    except Task.DoesNotExist:
        return HttpResponse("Task does not exist")


def update_task(request):
    task = Task.objects.get(pk=5)
    task.title = "This is a modified task title"
    task.save()
    return redirect("task_list")


def add_task_form(request):
    if request.method == "POST":
        form  = TaskForm(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect("task_list")
    else:
        form = TaskForm()
        return render(request, "add_task.html", {"formx": form})
