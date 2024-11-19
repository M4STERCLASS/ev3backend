from django.db import models

class Cliente(models.Model):
    cliente_id = models.IntegerField(primary_key=True)  # Clave primaria definida
    edad = models.FloatField(null=True, blank=True)
    genero = models.CharField(max_length=10, null=True, blank=True)
    saldo = models.FloatField(null=True, blank=True)
    activo = models.BooleanField(default=False)
    nivel_de_satisfaccion = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.cliente_id} - {self.genero}"
