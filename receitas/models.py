from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.


class Alura_receita(models.Model):
    nome_receita = models.CharField(max_length=100)
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    modo_preparo = models.TextField()
    ingredientes = models.TextField()
    data = models.DateTimeField(default=datetime.now, blank=True)
    pessoa = models.ForeignKey(User, on_delete=models.CASCADE)
    publicada = models.BooleanField(default=False)
    foto_receita = models.ImageField(upload_to='fotos/%d/%m/%Y/', blank=True)

    def __str__(self):
        return self.nome_receita
