from django.db import models

class Acudiente(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Pago(models.Model):
    acudiente = models.ForeignKey(Acudiente, on_delete=models.CASCADE)
    fecha = models.DateField()
    monto = models.IntegerField()
    pagado = models.BooleanField(default=False)

    def __str__(self):
        return "{} - {} - {}".format(self.acudiente, self.monto, self.fecha)


class Equipo(models.Model):
    name = models.CharField(max_length=30)
    entrenador = models.CharField(max_length=30)

    def __str__(self):
        return "{} - {}".format(self.name, self.entrenador)

class Jugador(models.Model):
    acudiente = models.ForeignKey(Acudiente, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, default=None, null=True, blank=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=30)
    altura = models.IntegerField()

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Subscripcion(models.Model):
    pago = models.ForeignKey(Pago, on_delete=models.CASCADE)
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)
    fecha = models.DateField()

    def __str__(self):
        return "{} - {} - {}".format(self.fecha, self.jugador, self.pago)

