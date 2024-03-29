from django.db import models


#Clases de agencias
class agencias(models.Model):
    nombre = models.CharField(max_length=48)
    tipo = models.CharField(max_length=48)
    id = models.CharField(max_length=48, primary_key=True)

    def __str__(self):
        return f"{self.nombre}"
    
    class Meta:
            verbose_name = "Agencia"
            verbose_name_plural = "Agencias"

#Clases de nuevos empleados 
class staff(models.Model):
    nombre = models.CharField(max_length=48)
    apellido = models.CharField(max_length=48)  
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
            verbose_name = "Staff"
            verbose_name_plural = "Staff"

#Clases de cursos
class Cursos(models.Model):
    curso = models.CharField(max_length=48) 
    comision = models.IntegerField()  

    def __str__(self):
        return self.curso
    

#Clases de nuevos usuarios a la plataforma
class Usuario(models.Model):
    nombre_agencia = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=100)



