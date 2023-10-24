from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Personas(models.Model):
    numero_documento = models.BigIntegerField(unique=True, primary_key=True, validators=[MinValueValidator(limit_value=6000000)])
    nombre_completo = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.nombre_completo} {self.numero_documento}'

class Email(models.Model):
    email = models.EmailField(unique=True)
    persona = models.ForeignKey(Personas, on_delete=models.CASCADE, related_name='emails',)

    def __str__(self):
        return f'{self.email} {self.persona}'

class Telefono(models.Model):
    telefono = models.BigIntegerField(validators=[
        MinValueValidator(3000000000),
        MaxValueValidator(3509999999)
    ])
    persona = models.ForeignKey(Personas, on_delete=models.CASCADE, related_name='telefonos')

    def __str__(self):
        return f'{self.telefono} {self.persona}'