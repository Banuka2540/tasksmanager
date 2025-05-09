from django.shortcuts import render, redirect
from .models import Task
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def home(request):
    return render(request, 'tasks/home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'tasks/register.html', {'form': form})

# User Dashboard
@login_required
def dashboard(request):
    user_tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/dashboard.html', {'tasks': user_tasks})

# Add Task
@login_required
def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        due_date = request.POST['due_date']
        Task.objects.create(
            title=title, description=description, due_date=due_date, user=request.user
        )
    user_tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/add_task.html', {'tasks': user_tasks})

