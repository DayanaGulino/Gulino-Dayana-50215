from django.urls import path
from .views import *

from django.contrib.auth.views import LogoutView



urlpatterns = [
    #___________principales_______
    path('', home, name="home"),
    path('Inicio', Inicio, name="Inicio"),
    path('cursos/', Cursos, name="Cursos"),
    path('agencias/', Agencias, name="Agencias"),
    path('contacto/', Contacto, name='Contacto'),
    path('entregables/', Entregables, name="Entregables"),
#__________- ingreso y egreso de la plataforma________

    path('registroForm', registroForm, name='registroForm'),
    path('login', formLogin, name='login'),
    path('logout', LogoutView.as_view (template_name= "aplicacion/logout.html"), name='logout'),
    
#__________- formularios___________
    path('cursoForm/', cursoForm, name="cursoForm/"),
    path('crear_usuario/', crear_usuario, name='crear_usuario/'),
    path('curso_update/<id_curso>/', updateCurso, name='curso_update/'),
    path('curso_delete/<id_curso>/', deleteCurso, name='curso_delete/'),
    path('Agencia_update/<int:id_agencia>/', updateAgencia, name='agencia_update'),
    path('Agencia_delete/<int:id_agencia>/', deleteAgencia, name='agencia_delete'),
    path('crear_staff/', crear_staff, name='crear_staff/'),

#____________Cursos e información de destinos________
    path('Australia/', Australia, name="Australia"),

#_____________ Evaluaciones________
#________No he agregado mas de una ya que dependerá de la evaluación que realicen mis líderes______
    path('Evaluaciones/', Evaluacion , name="Evaluaciones/"),

#__________Editar perfil________
 path('perfil/', editProfile, name='perfil'),

]