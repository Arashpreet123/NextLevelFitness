from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import CarouselImage

# Create your views here.

def home(request):
    template = loader.get_template('home.html')
    images = CarouselImage.objects.all()
    return render(request, 'home.html', {'images' : images})


def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # You can process the form data here (e.g., send an email)
        return render(request, 'contact.html', {'success': True})
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())

def class_schedule(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # You can process the form data here (e.g., send an email)
        return render(request, 'contact.html', {'success': True})
    template = loader.get_template('class_schedule.html')
    return HttpResponse(template.render())