from django.shortcuts import render, redirect
from .models import *

def index(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, 'course.html', context)

def create(request):
    Course.objects.create(
        name = request.POST['name'],
        description = request.POST['description']
    )
    return redirect('/courses')

def show(request, id):
    if request.method == 'GET':
        context = {
            "course": Course.objects.get(id=id)
        }
        return render(request, 'destroy.html', context)

def destroy(request, id):
    if request.method == 'GET':
        context = {
            "course": Course.objects.get(id=id)
        }
        return render(request, 'destroy.html', context)

    if request.method == 'POST':
        courses = Course.objects.get(id=id)
        courses.delete() 
        return redirect('/courses')

