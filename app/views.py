from django.shortcuts import render

# Create your views here.
def money(request):
    return render (request,'money.html')
def paisa(request):
    return render (request,'paisa.html')