from django.db import models

class agencias(models.Model):
    nombre = models.CharField(max_length=48)
    tipo = models.CharField(max_length=48)
    id = models.CharField(max_length=48, primary_key=True)

    def __str__(self):
        return f"{self.nombre}"
    
    class Meta:
            verbose_name = "Agencia"
            verbose_name_plural = "Agencias"

class staff(models.Model):
    nombre = models.CharField(max_length=48)
    apellido = models.CharField(max_length=48)  
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
            verbose_name = "Staff"
            verbose_name_plural = "Staff"


class Curso(models.Model):
    nombre = models.CharField(max_length=48) 
    comision = models.IntegerField()  

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    nombre_agencia = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=100)
    
