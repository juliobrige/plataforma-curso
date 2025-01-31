
from django.urls import path
from . import views

urlpatterns = [
    path ('', views.home, name='home'),
    path('', views.lista_cursos, name='lista_cursos'),
    path('curso/<int:curso_id>/', views.detalhes_curso, name='detalhes_curso'),
    path('aula/<int:aula_id>/', views.aula, name='aula'),
]