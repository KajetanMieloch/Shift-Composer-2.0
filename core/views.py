from django.shortcuts import render

def index(request):
    return render(request, 'core/index.html')

def backgroundtest(request):
    return render(request, 'core/backgroundtest.html')