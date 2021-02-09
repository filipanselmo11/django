from django.db import models


class Heroi(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.CharField(max_length=30)

    def __str__(self):
        return self.nome


class Item(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.CharField(max_length=30)

    def __str__(self):
        return self.nome
