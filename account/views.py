from django.shortcuts import render,redirect


# Create your views here.
def index(request):
    return render(request,"index.html")

def registerResturant(request):
    return render(request,"ResturantRegister.html")

def userRegister(request):
    return render(request,'userRegister.html')
