from django.db import models
from usuarios.models import Usuario

class Curso(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    instrutor = models.ForeignKey(Usuario, on_delete=models.CASCADE)  # Agora User está definido
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    capa = models.ImageField(upload_to='cursos/capas/')

    def __str__(self):
        return self.titulo

class Modulo(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='modulos')
    titulo = models.CharField(max_length=100)
    ordem = models.PositiveIntegerField()

    def __str__(self):
        return self.titulo

class Aula(models.Model):
    modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE, related_name='aulas')
    titulo = models.CharField(max_length=100)
    conteudo_video = models.FileField(upload_to='cursos/videos/')
    conteudo_texto = models.TextField(blank=True)

    def __str__(self):
        return self.titulo

class Matricula(models.Model):
    aluno = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    data_matricula = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.aluno.username} - {self.curso.titulo}"