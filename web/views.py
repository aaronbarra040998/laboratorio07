from django.shortcuts import render, redirect
from django.views import View
from django.shortcuts import get_object_or_404
from .models import *
from .forms import *

class AlumnoView(View):
    
    def get(self, request):
        listaAlumnos = TblAlumno.objects.all()
        formAlumno = AlumnoForm()
        context = {
            'alumnos' : listaAlumnos,
            'formAlumno': formAlumno
        }
        return render(request, 'index.html', context)

    def post(self, request):
        formAlumno = AlumnoForm(request.POST)
        if formAlumno.is_valid():
            formAlumno.save()
            return redirect('/')

class AlumnoDeleteView(View):
    def post(self, request, pk):
        alumno = get_object_or_404(TblAlumno, pk=pk)
        alumno.delete()
        return redirect('/')

class ProfesorView(View):
    def get(self, request):
        listaProfesores = TblProfesor.objects.all()
        formProfesor = ProfesorForm()
        context = {
            'profesores': listaProfesores,
            'formProfesor': formProfesor
        }
        return render(request, 'profesor.html', context)
    
    def post(self, request):
        formProfesor = ProfesorForm(request.POST)
        if formProfesor.is_valid():
            formProfesor.save()
            return redirect('web:index2')
        else:
            return render(request, 'profesor.html', {'formProfesor': formProfesor})

class ProfesorDeleteView(View):
    def post(self, request, pk):
        profesor = get_object_or_404(TblProfesor, pk=pk)
        profesor.delete()
        return redirect('web:index2')

