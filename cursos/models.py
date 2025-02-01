from django.db import models
from usuarios.models import Usuario

class Curso(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    instrutor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    capa = models.ImageField(upload_to='capas/')

class Modulo(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    ordem = models.PositiveIntegerField()

class Aula(models.Model):
    modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    conteudo_video = models.FileField(upload_to='videos/')
    conteudo_texto = models.TextField(blank=True)

class Matricula(models.Model):
    aluno = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    data_matricula = models.DateTimeField(auto_now_add=True)