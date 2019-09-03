from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
def home_page(request):
    return render(request, 'home.html', {})

def about_page(request):
    return render(request, 'about.html', {})
