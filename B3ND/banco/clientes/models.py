from django.db import models

class Cliente(models.Model):
    GENERO_CHOICES = [('M', 'Masculino'), ('F', 'Femenino')]
    SATISFACCION_CHOICES = [(i, str(i)) for i in range(1, 6)]

    cliente_id = models.AutoField(primary_key=True)
    edad = models.FloatField(null=True, blank=True)
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES, null=True, blank=True)
    saldo = models.FloatField(null=True, blank=True)
    activo = models.BooleanField(default=False)
    nivel_de_satisfaccion = models.IntegerField(choices=SATISFACCION_CHOICES, null=True, blank=True)

    def __str__(self):
        return f'Cliente {self.cliente_id}'
