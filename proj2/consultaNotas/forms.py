from django import forms
from .models import Alumno, Curso, NotasAlumnosPorCurso
from django.core.validators import MaxValueValidator

#El formulario solo permitirá subir notas, pues agregar alumnos
#y cursos no debería ser una tarea del usuario
class AgregarNotasForm(forms.ModelForm):
    codigo_curso = forms.CharField(max_length=10, label="Código del curso")
    cui_alumno = forms.IntegerField(validators=[
        MaxValueValidator(99999999)
    ])

    class Meta:
        model = NotasAlumnosPorCurso
        fields = ['codigo_curso', 'cui_alumno', 'nota']

        def clean_codigo_curso(self):
            codigo = self.cleaned_data.get('codigo_curso')
            if not Curso.objects.filter(codigo=codigo).exists():
                raise forms.ValidationError("No existe este curso.")
            return codigo
        
        def clean_cui_alumno(self):
            cui = self.cleaned_data.get('cui_alumno')
            if not Alumno.objects.filter(cui=cui).exists():
                raise forms.ValidationError("El alumno con este CUI no existe.")
            return cui
        
        def save(self, commit=True):
            codigo = self.cleaned_data.get('codigo_curso')
            curso = Curso.objects.get(codigo=codigo)
            cui = self.cleaned_cui_alumno('cui_alumno')
            alumno = Alumno.objects.get(cui=cui)
            notaEnElCurso = super().save(commit=False)
            notaEnElCurso.curso = curso
            notaEnElCurso.alumno = alumno
            if commit:
                notaEnElCurso.save()
            return notaEnElCurso