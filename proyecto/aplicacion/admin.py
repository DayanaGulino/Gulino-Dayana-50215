from django.contrib import admin


# Register your models here.
from .models import *
admin.site.register(Cursos)
admin.site.register(staff)
admin.site.register(agencias)


