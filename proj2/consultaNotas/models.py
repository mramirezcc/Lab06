from django.db import models

class Alumno(models.Model):

    class Anio(models.IntegerChoices):
        PRIMERO = 1
        SEGUNDO = 2
        TERCERO = 3
        CUARTO = 4
        QUINTO = 5

    #Dado que un CUI empieza con el año de ingreso, no será
    #necesario considerar ceros a la izquierda
    cui = models.IntegerField(max_digits=8)
    nombre = models.CharField(max_length=100)
    anio = models.SmallIntegerField(choices=Anio.choices)

    def __str__(self):
        return self.nombre

class Curso(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class NotasAlumnosPorCurso(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    nota = models.DecimalField(max_value=20, decimal_places=1)

    def __str__(self):
        return f"{self.alumno.nombre} tiene una nota de {self.nota} en {self.curso.codigo}"