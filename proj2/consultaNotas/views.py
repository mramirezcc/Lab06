from django.shortcuts import render, redirect
from .forms import AgregarNotasForm, NotasAlumnosPorCurso

def agregar_nota(request):
    if request.method == 'POST':
        form = AgregarNotasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_notas')
    else:
        form = AgregarNotasForm()
        return render(request, 'consultaNotas/agregar_nota.html', {'form', form})

def lista_notas(request):
    notas = NotasAlumnosPorCurso(request)
    return render(request, 'consultaNotas/lista_notas.html', {'notas': notas})
