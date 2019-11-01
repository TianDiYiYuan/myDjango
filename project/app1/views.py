# -*-coding:utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("hello world!")

def detail(request,num,num2):
    return HttpResponse("detail-%d-%d" %(int(num),int(num2) ))
    #return HttpResponse(str(num))

from .models import Grades,Students

def grades(request):
    #去模板里取数据
    gradesList = Grades.objects.all()
    #将数传递给模板，模板在渲染页面，将渲染的页面传递给浏览器
    return render(request,'app1/grades.html',
    {"grades":gradesList})
    
def students(request):
    #去模板里取数据
    studentsList = Students.objects.all()
    #将数传递给模板，模板在渲染页面，将渲染的页面传递给浏览器
    return render(request,'app1/students.html',
    {"students":studentsList})
 

def gradeStudents(request,num):
    #去模板里取数据
    grade = Grades.objects.get(pk=int(num))

    studentsList = grade.students_set.all()
    #将数传递给模板，模板在渲染页面，将渲染的页面传递给浏览器
    return render(request,'app1/students.html',
    {"students":studentsList})