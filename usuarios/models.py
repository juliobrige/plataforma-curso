from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuarios(models.Model):  # Nome do modelo
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
class Usuario(AbstractUser):
    # Campos personalizados (opcional)
    telefone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username