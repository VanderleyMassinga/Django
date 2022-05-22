from turtle import ondrag
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=255, unique=True)
    body = models.TextField()
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo
