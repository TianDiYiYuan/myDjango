from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('<int:num>/<int:num2>/', views.detail,name='detail'),

    path('grades/', views.grades,name='grades'),
    path('students/', views.students,name='students'),
    path('grades/<int:num>/', views.gradeStudents,name='gradeStudents'),
]

