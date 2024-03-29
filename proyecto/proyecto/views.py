from django.template import Template, Context, loader
from django.http import HttpResponse
import datetime


#No dar importancia para el proyecto final_________________________
def saludar(request):
    return HttpResponse ("Bieenvenido a la comision 50215 - clase Django")

def bienvenida(request, nombre):
    respuesta = f"te damos la bienvenida {nombre}"
    return HttpResponse (respuesta)

def bienvenido_template(request):
    miHtml = open("D:/Users/dayan/Desktop/Python/proyecto/proyecto/plantillas/bienvenido.html")
    plantilla = Template(miHtml.read())
    miHtml.close()
    contexto = Context() 
    respuesta = plantilla.render(contexto)
    return HttpResponse(respuesta)

def bienvenido_template1(request):
    hoy = datetime.datetime.now()
    nombre = "Amadeus"
    apellido = "Mozart"
    notas = [7, 8, 9, 6, 2]
    contexto = {"nombre": nombre , "apellido": apellido, "hoy": hoy, "notas": notas}
    plantilla =loader.get_template("bienvenido1.html")
    respuesta =plantilla.render(contexto)

    return HttpResponse(respuesta)
