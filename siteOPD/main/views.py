from django.shortcuts import render


def registration(request):
    return render(request, 'main/registration.html')


def about(request):
    return render(request, 'main/about.html')


def recommendations(request):
    return render(request, 'main/recommendations.html')


def friends(request):
    return render(request, 'main/friends.html')


def account(request):
    return render(request, 'main/account.html')
