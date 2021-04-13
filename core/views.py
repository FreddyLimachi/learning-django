from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def store(request):
    return render(request, "store.html")

def contact(request):
    return HttpResponse("Contacto")

def sample(request):
    return HttpResponse("Sample")