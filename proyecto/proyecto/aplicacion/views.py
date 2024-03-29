from django.shortcuts import render
from .models import *
from .forms import *


# Create your views here.
def home (request):
    return render(request, "aplicacion/index.html")



def Cursos(request):  
    contexto = {'cursos': Curso.objects.all()}
    return render(request, "aplicacion/Cursos.html", contexto)

def Agencias (request):
    return render(request, "aplicacion/Agencias.html")

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

def cursoForm(request):
    if request.method == "POST":
        miForm = CursoForm(request.POST)
        if miForm.is_valid():
            curso_nombre = miForm.cleaned_data.get("nombre")
            curso_numero = miForm.cleaned_data.get("comision")
            contexto = {'cursos': Curso.objects.all()}
            nuevo_curso = Curso(nombre=curso_nombre, comision=curso_numero)
            nuevo_curso.save()
            return render(request, "aplicacion/Cursos.html", contexto)
    else:
        miForm = CursoForm()
    return render(request, "aplicacion/cursoForm.html", {"form": miForm})

def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            nombre_agencia = form.cleaned_data.get("nombre_agencia")
            contraseña = form.cleaned_data.get("contraseña")
            nuevo_usuario = Usuario(nombre_agencia=nombre_agencia, contraseña=contraseña)
            nuevo_usuario.save()
            return render(request,'aplicacion/UsuariosForm.html')
    else:
        form = UsuarioForm()
    return render(request, 'aplicacion/UsuariosForm.html', {'form': form})

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
    return render(request, "aplicacion/index.html", {'form': form})

def crear_agencia(request):
    if request.method == 'POST':
        form = AgenciaForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            tipo = form.cleaned_data.get("tipo")
            id = form.cleaned_data.get("id")
            nueva_agencia = agencias(nombre=nombre, tipo=tipo, id=id)
            nueva_agencia.save()
            return render(request, "aplicacion/index.html",)
    else:
        form = AgenciaForm()
    return render(request, 'aplicacion/index', {'form': form})

def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            curso_nombre = form.cleaned_data.get("curso")
            curso_numero = form.cleaned_data.get("comision")
            nuevo_curso = Cursos(curso=curso_nombre, comision=curso_numero)
            nuevo_curso.save()
            return render(request, "aplicacion/index.html",)
    else:
        form = CursoForm()
    return render(request, "aplicacion/index.html", {'form': form})

def registroForm(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            nombre_agencia = form.cleaned_data.get('nombre_agencia')
            contraseña = form.cleaned_data.get('contraseña')  
            confirmar_contraseña = form.cleaned_data.get('confirmar_contraseña')
            return render(request, "aplicacion/index.html")
    else:
        form = RegistroForm()
    return render(request, 'aplicacion/cursoForm.html', {'form': form})


def formLogin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)  # Aquí utilizamos LoginForm en lugar de formLogin
        if form.is_valid():
            nombre_agencia = form.cleaned_data['nombre_agencia']
            contraseña = form.cleaned_data['contraseña']
            # Aquí puedes procesar la autenticación o cualquier lógica adicional
            return render(request, "aplicacion/index.html")
    else:
        form = LoginForm()  # Aquí utilizamos LoginForm en lugar de formLogin
    return render(request, 'aplicacion/formLogin.html', {'form': form})



#_________Cursos

def Australia (request):
    return render(request, "aplicacion/Cursos_info/Australia.html")

def Evaluacion (request):
    return render(request, "aplicacion/Evaluacion/Evaluacion.html")
