import datetime
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.template import loader
from django.urls import reverse
from django.shortcuts import get_object_or_404, render

from .models import Teacher, OfficeHour, Student
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return HttpResponse("Hello World")

def detail(request, teacher_name):
    template = loader.get_template('hippoqueue/detail.html')
    q = User.objects.filter(username=teacher_name)
    t = q[0].teacher
    if request.user.is_authenticated and request.user.username == teacher_name:
        template = loader.get_template('hippoqueue/detail.html')
        q = User.objects.filter(username=teacher_name)
        t = q[0].teacher
        if t.officehour_set.count() > 0:
            context = {
                'teacher_name':
                teacher_name,
                'teacher' :
                True,
                'started':
                True,
                'officehour':
                t.officehour_set.all()[0]
            }
        else:
            context = {
                'teacher_name':
                teacher_name,
                'teacher' :
                True
            }
        return HttpResponse(template.render(context, request))
    else:
        context = {
            'teacher_name':
            teacher_name,
            'officehour':
            t.officehour_set.all()[0]
        }
        return HttpResponse(template.render(context, request))

        

def start(request, teacher_name):
    if request.user.is_authenticated and request.user.username == teacher_name:
        q = User.objects.filter(username=teacher_name)
        t = q[0].teacher
        if t.officehour_set.count() == 0:
            t.officehour_set.create(start = datetime.datetime.now(), length = 2)
        else:
            print("Has office hours")
        return HttpResponse("Office hour started")
    else:
        return HttpResponseForbidden("You do not have permission to do that")

def add(request, teacher_name):
    print(request.POST['fname'])
    q = User.objects.filter(username=teacher_name)
    t = q[0].teacher
    oh = t.officehour_set.all()[0]
    oh.student_set.create(fname = request.POST['fname'], lname = request.POST['lname'])
    return HttpResponseRedirect(reverse('hippoqueue:detail', args=(teacher_name,)))

def remove(request, teacher_name, student_id):
    q = User.objects.filter(username=teacher_name)
    t = q[0].teacher
    oh = t.officehour_set.all()[0]
    student = Student.objects.filter(id = student_id, officeHour = oh)
    student.delete()
    return HttpResponseRedirect(reverse('hippoqueue:detail', args=(teacher_name,)))
