from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "neocycle/index.html" )

def aboutus(request):
    return render(request, "neocycle/aboutus.html")

def products(request):
    return render(request, "neocycle/products.html")

def blog(request):
    return render(request, "neocycle/blog.html")

def contact(request):
    return render(request, "neocycle/contact.html")

def wishlist(request):
    return render(request, "neocycle/wishlist.html")

def login(request):
    return render(request, "neocycle/login.html")


    