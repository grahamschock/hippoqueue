from django.urls import path

from . import views

app_name = "hippoqueue"
urlpatterns = [
    path('', views.index, name='index'),
    path('oh/<str:teacher_name>', views.detail, name = 'detail'),
    path('oh/<str:teacher_name>/start/', views.start, name='start'),
    path('oh/<str:teacher_name>/add/', views.add, name='add'),
    path('oh/<str:teacher_name>/remove/<int:student_id>', views.remove, name='remove')
]
