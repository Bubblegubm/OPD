from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def registration(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account')
        else:
            error = 'Форма была неверной'

    form = TaskForm()
    tasks = {
        'form': form,
        'error': error
    }
    return render(request, 'main/registration.html', tasks)


def about(request):
    return render(request, 'main/about.html')


def recommendations(request):
    return render(request, 'main/recommendations.html')


def friends(request):
    return render(request, 'main/friends.html')


def account(request):
    return render(request, 'main/account.html')
