from django.urls import path
from .views import *



urlpatterns = [
    #___________principales
    path('', home, name="home"),
    path('Inicio', Inicio, name="Inicio"),
    path('cursos/', Cursos, name="Cursos"),
    path('agencias/', Agencias, name="Agencias"),
    path('contacto/', Contacto, name='Contacto'),
    path('entregables/', Entregables, name="Entregables"),
#__________- ingreso

    path('registroForm', registroForm, name='registroForm'),
    path('login', formLogin, name='login'),
#__________- formularios
    path('cursoForm/', cursoForm, name="cursoForm/"),
    path('crear_usuario/', StaffForm, name='crear_usuario/'),
    path('crear_staff/', crear_staff, name='crear_staff/'),
    path('crear_agencia/', crear_agencia, name='crear_agencia/'),
    path('crear_curso/', crear_curso, name='crear_curso/'),

#____________Cursos
    path('Australia/', Australia, name="Australia"),
#_____________ Evaluaciones
    path('Evaluaciones/', Evaluacion , name="Evaluaciones/"),

]