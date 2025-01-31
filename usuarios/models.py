from django.db import models

from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    telefone = models.CharField(max_length=15, blank=True)
    is_instrutor = models.BooleanField(default=False)
