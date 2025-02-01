from django.contrib import admin
from .models import Curso, Modulo, Aula, Matricula

admin.site.register(Curso)
admin.site.register(Modulo)
admin.site.register(Aula)
admin.site.register(Matricula)
