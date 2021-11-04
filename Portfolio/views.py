from django.shortcuts import render


def index(request):
    return render(request, 'Core_app/index.html')
