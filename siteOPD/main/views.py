from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CreateUserForm, UserInfoForm
from .models import Recommendation, UserInfo, Friends
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout




def registration(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form': form}
    return render(request, 'main/registration.html', context)


def about(request):
    return render(request, 'main/about.html')


def recommendations(request):
    rec = Recommendation.objects.all()
    return render(request, 'main/recommendations.html', {'rec': rec})


def friends(request):
    friend = Friends.objects.all()
    return render(request, 'main/friends.html', {'friend': friend})


def account(request):
    form = UserInfoForm()
    if request.method == 'POST':
        form = UserInfoForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}

    return render(request, 'main/account.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

    context = {}
    return render(request, 'main/login.html', context)


def logoutPage(request):
    logout(request)
    return redirect('login')