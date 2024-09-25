from django.shortcuts import render

# Create your views here.


def homePage(request):
    return render(request, 'home.html')


def navebar(request):
    return render(request, 'navebar.html')


def contactPage(request):
    return render(request, 'contact.html')


def registerPage(request):
    return render(request, 'register.html')


def loginPage(request):
    return render(request, 'login.html')


def eventPage(request):
    return render(request, 'event.html')


def productPage(request):
    return render(request, 'product.html')
