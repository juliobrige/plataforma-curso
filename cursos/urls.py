
from django.urls import path
from . import views

urlpatterns = [
    path ('', views.home, name='home'),
    path('detalhes_curso/<int:curso_id>/', views.detalhes_curso, name='detalhes_curso'),
    path('lista_cursos/', views.lista_cursos, name='lista_cursos'),
     path('aula/', views.aula_view, name='aula'),
    path('', views.index, name='home'),
    path('matricular/<int:curso_id>/', views.matricular, name='matricular'),
    path('dashboard/', views.dashboard, name='dashboard'),
     path('index/', views.index, name='index'),
    path('quiz/<int:pk>/', views.quiz_view, name='quiz'),

]