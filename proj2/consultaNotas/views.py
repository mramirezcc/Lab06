from django.shortcuts import render, redirect
from .forms import AgregarNotasForm, NotasAlumnosPorCurso

def agregar_nota(request):
    if request.method == 'POST':
        form = AgregarNotasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_notas')
        form = AgregarNotasForm()
        return render(request, 'notas/agregar_nota.html', {'form': form})

    else:
        form = AgregarNotasForm()
        return render(request, 'notas/agregar_nota.html', {'form': form})

def lista_notas(request):
    notas = NotasAlumnosPorCurso(request)
    return render(request, 'notas/lista_notas.html', {'notas': notas})
