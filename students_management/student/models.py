from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    COURSES = [
        ('AI', 'Professional Diploma in Artificial Intelligence'),
        ('IT', 'Professional Diploma in Data Analytics'),
        ('ECE', 'Professional Diploma in Software Engineering'),
        ('ME', 'Professional Diploma in Blockchain Technology'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    student_id = models.CharField(max_length=150, unique=True)
    names = models.CharField(max_length=150)
    course = models.CharField(max_length=10, choices=COURSES)
    email_address = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.names


class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    studentId = models.CharField(max_length=50, unique=True)
    date = models.DateTimeField(unique=True)
    studentName = models.CharField(max_length=100, unique=True)

    def __str__(self):
        
        return self.studentName


