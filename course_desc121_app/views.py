from django.shortcuts import render, HttpResponse, redirect
from . models import CourseManager, Course
from django.contrib import messages

def index(request):
    print(request)     
    context = {
        'courses': Course.objects.all()
    }

    return render (request, 'index.html', context)

def add_course(request):
    errors = Course.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        added_course = Course.objects.create(name=request.POST['name'], description=request.POST['desc'])
        print(added_course)
        print("**Courses***")
        messages.success(request, "Course successfully added")    
        return redirect('/')

def d_course(request, id):
    print("You will delete this course")
    context = {
        'd_course': Course.objects.get(id=id)
    }
    return render(request, 'delete_course.html', context)       

def delete_course(request, id): 
    print("Deleting")
    course_to_delete = Course.objects.get(id=id)
    course_to_delete.delete()
    return redirect('/')
        
    


# Create your views here.
