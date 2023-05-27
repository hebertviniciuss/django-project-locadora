from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome

class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    valor = models.IntegerField()
    categoria = models.OneToOneField(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Locacao(models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateField() 
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome