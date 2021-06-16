from django.shortcuts import render

# Create your views here.

def concrete (request):
    return render(request, "concrete/home.html")