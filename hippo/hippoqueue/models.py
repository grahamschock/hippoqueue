from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Teacher(models.Model):
    subject = models.CharField(max_length = 50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class OfficeHour(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete =
                                models.CASCADE)
    start = models.DateTimeField()
    length = models.IntegerField(default=1)

class Student(models.Model):
    officeHour = models.ForeignKey(OfficeHour, on_delete=
                                   models.CASCADE)
    fname = models.CharField(max_length = 50)
    lname = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
