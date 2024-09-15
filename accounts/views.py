from django.shortcuts import render

def home_page(request):
    return render(request, 'home_page.html')

def contact_page(request):
    return render(request, 'contact_page.html')

# Create your views here.
