from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout


def home(request):
    return render(request, 'tasks/home.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def logged_out(request):
    logout(request)
    return render(request, 'tasks/logged_out.html')


# Dashboard with tasks
@login_required
def dashboard(request):
    user_tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/dashboard.html', {'tasks': user_tasks})


# Add Task + show existing tasks
@login_required
def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        due_date = request.POST['due_date']
        Task.objects.create(
            title=title, description=description, due_date=due_date, user=request.user
        )
        return redirect('add_task')  # refresh after adding
    user_tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/add_task.html', {'tasks': user_tasks})


# Delete Task
@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.delete()
    return redirect('add_task')
