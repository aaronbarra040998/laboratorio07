from django.urls import path

from . import views

app_name = 'web'

urlpatterns = [
    path('', views.AlumnoView.as_view(),name='index'),
    path('agregar-alumno/', views.AlumnoView.as_view(), name='agregar-alumno'),
    path('delete-alumno/<int:pk>/', views.AlumnoDeleteView.as_view(), name='delete_alumno'),

    path('profesor/', views.ProfesorView.as_view(), name='index2'),
    path('agregar-profesor/', views.ProfesorView.as_view(), name='agregar-profesor'),
    path('delete-profesor/<int:pk>/', views.ProfesorDeleteView.as_view(), name='delete_profesor'),
]