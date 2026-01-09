from django.shortcuts import render

def home(request):
    return render(request, 'myprofile/home.html')

def about(request):
    return render(request, 'myprofile/about.html')

def gallery(request):
    return render(request, 'myprofile/gallery.html')
