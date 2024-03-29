from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import *
from .models import Cursos as CursoModel
from .forms import *

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

#Principales vistas de la aplicación web______________________________
def home (request):
    return render(request, "aplicacion/index.html")


def Cursos(request):  
    contexto = {'cursos': CursoModel.objects.all()}
    return render(request, "aplicacion/Cursos.html", contexto)

def Agencias(request):
    agencias = Usuario.objects.all()  # Obtener todas las agencias desde el modelo Usuario
    return render(request, 'aplicacion/agencias.html', {'agencias': agencias})


def Entregables (request):
    return render(request, "aplicacion/Entregables.html")

def Contacto (request):
    return render(request, "aplicacion/Contacto.html")

def Inicio (request):
    return render(request, "aplicacion/Inicio.html")

def login_view(request):
    return render(request, 'formLogin.html')

def registro_view(request):
    return render(request, 'formRegistro.html')

#_________________forms

#_____Creación nuevos cursos______
def cursoForm(request):
    if request.method == "POST":
        miForm = CursoForm(request.POST)
        if miForm.is_valid():
            curso_nombre = miForm.cleaned_data.get("curso")
            curso_numero = miForm.cleaned_data.get("comision")
            nuevo_curso = CursoModel(curso=curso_nombre, comision=curso_numero)
            nuevo_curso.save()
            return render(request, "aplicacion/index.html")
    else:
        miForm = CursoForm()
    return render(request, "aplicacion/cursoForm.html", {"form": miForm})


#_____Modificación y eliminación de cursos_____
def updateCurso(request, id_curso):
    curso = CursoModel.objects.get(id=id_curso)
    
    if request.method == "POST":
        miForm = CursoForm(request.POST)
        if miForm.is_valid():
            curso.curso = miForm.cleaned_data.get("curso")
            curso.comision = miForm.cleaned_data.get("comision")
            curso.save()
            
            cursos = CursoModel.objects.all().order_by("id")
            contexto = {'cursos': cursos}
            return render(request, "aplicacion/Cursos.html", contexto)
    else:
        miForm = CursoForm(initial={'curso': curso.curso, 'comision': curso.comision})
    return render(request, "aplicacion/cursoForm.html", {'form': miForm})


def deleteCurso(request, id_curso):
    curso = CursoModel.objects.get(id=id_curso)
    curso.delete()
    return redirect(reverse_lazy ('Cursos'))

#________-Creación de agencias_______
def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            nombre_agencia = form.cleaned_data.get("nombre_agencia")
            contraseña = form.cleaned_data.get("contraseña")
            nuevo_usuario = Usuario(nombre_agencia=nombre_agencia, contraseña=contraseña)
            nuevo_usuario.save()
            
            agencias = Usuario.objects.all()
            return render(request, 'aplicacion/Agencias.html', {'agencias': agencias})
    else:
        form = UsuarioForm()
    return render(request, 'aplicacion/UsuariosForm.html', {'form': form})

#_____Modificación y eliminación de agencias_____


def updateAgencia(request, id_agencia):
    agencia = Usuario.objects.get(id=id_agencia)
    
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            agencia.nombre_agencia = form.cleaned_data.get("nombre_agencia")
            agencia.contraseña = form.cleaned_data.get("contraseña")
            agencia.save()
            
            agencias = Usuario.objects.all()
            return render(request, "aplicacion/Agencias.html", {'agencias': agencias})
    else:
        form = UsuarioForm(initial={'nombre_agencia': agencia.nombre_agencia, 'contraseña': agencia.contraseña})
    return render(request, "aplicacion/UsuariosForm.html", {'form': form})

def deleteAgencia(request, id_agencia):
    agencia = Usuario.objects.get(id=id_agencia)
    agencia.delete()
    return redirect('Agencias')

#_____Creación de nuevos empleados de GrowPro Agent_____

def crear_staff(request):
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            apellido = form.cleaned_data.get("apellido")
            email = form.cleaned_data.get("email")
            nuevo_staff = staff(nombre=nombre, apellido=apellido, email=email)
            nuevo_staff.save()
            return render(request, "aplicacion/index.html",)
    else:
        form = StaffForm()
    return render(request, "aplicacion/staffForm.html", {'form': form})


#________________________Ingreso y egresos de la plataforma

def registroForm(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            nombre_agencia = form.cleaned_data.get('nombre_agencia')
            contraseña = form.cleaned_data.get('contraseña')  
            confirmar_contraseña = form.cleaned_data.get('confirmar_contraseña')
            return redirect('Inicio')
    else:
        form = RegistroForm()  
    return render(request, 'aplicacion/registroForm.html', {'form': form})



def formLogin(request):
    if request.method == 'POST':
        nombre_agencia = request.POST['username']
        contraseña = request.POST['password']
        user = authenticate(request, username=nombre_agencia, password=contraseña)
        if user is not None:
            login(request, user)
            return redirect(reverse_lazy('Inicio')) 
        else:
            return redirect(reverse_lazy('login'))
    else:
        form = AuthenticationForm()
    return render(request, 'aplicacion/formLogin.html', {'form': form})

def logout_request(request):
    logout_request
    return render(request, "aplicacion/logout.html")

#_________edición del perfil___________

def editProfile(request):
    if request.method == "POST":
        miForm = UserEditForm(request.POST)
        if miForm.is_valid():
            # Procesar el formulario aquí
            return redirect(reverse_lazy('Inicio'))
    else:
        miForm = UserEditForm()

    return render(request, "aplicacion/editProfile.html", {'form': miForm})


#_________Información de Cursos_______
#_______La idea es agregar con el tiempo todos los campos faltantes de información con cada destino según lo indique mi líder de la empresa, por eso los botones están vacíos en la mayoría de los destinos, pero puse los siguientes a modo de ejemplo________

def Australia (request):
    return render(request, "aplicacion/Cursos_info/Australia.html")

def Evaluacion (request):
    return render(request, "aplicacion/Evaluacion/Evaluacion.html")
