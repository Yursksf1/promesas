from django.db import models
from django.contrib.auth.models import User, AbstractUser


class Acudiente(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Pago(models.Model):
    acudiente = models.ForeignKey(Acudiente, on_delete=models.CASCADE)
    fecha = models.DateField()
    monto = models.IntegerField(default=0, null=True, blank=True)
    pagado = models.BooleanField(default=False)

    def __str__(self):
        return "{} - {} - {}".format(self.acudiente, self.monto, self.fecha)


class Equipo(models.Model):
    name = models.CharField(max_length=30)
    entrenador = models.CharField(max_length=30)

    def __str__(self):
        return "{} - {}".format(self.name, self.entrenador)

class Jugador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, null=True, blank=True)
    genero = models.CharField(max_length=30, null=True, blank=True, default=None)
    altura = models.IntegerField()

    class Meta:
        verbose_name = "Jugador"
        verbose_name_plural = "Jugadores"


    def __str__(self):
        return "{} {} ".format(self.user.first_name, self.user.last_name)

    def edad(self):
        # todo: define function to get age
        birhtday = '13'
        return birhtday

class Subscripcion(models.Model):
    pago = models.ForeignKey(Pago, on_delete=models.CASCADE)
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)
    fecha = models.DateField()

    class Meta:
        verbose_name = "Subscription"
        verbose_name_plural = "Subscripciones"


    def __str__(self):
        return "{} - {} - {}".format(self.fecha, self.jugador, self.pago)

class Horario_partido(models.Model):
    partido = models.CharField(max_length=30)
    uniforme = models.CharField(max_length=30)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    primer_equipo = models.ForeignKey(Equipo, related_name="Horario_primer_equipo", on_delete=models.CASCADE, null=True)
    segundo_equipo = models.ForeignKey(Equipo, related_name="Horario_segundo_equipo", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "{} - {} - {} - {} ".format(self.partido, self.uniforme, self.fecha_inicio, self.fecha_fin)


class Entrenamientos_jugador(models.Model):
    Cantidad_partidos = models.ForeignKey(Horario_partido, on_delete=models.CASCADE)
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)
    categoria = models.CharField(max_length=30)
    edad = models.IntegerField()

    class Meta:
        verbose_name = "Entrenamientos_jugador"
        verbose_name_plural = "Entrenamientos_jugadores"


    def __str__(self):
        return "{} - {} - {} - {} ".format(self.Cantidad_partidos, self.categoria, self.edad, self.jugador,)


class Resultado(models.Model):
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)
    partido = models.ForeignKey(Horario_partido, on_delete=models.CASCADE)
    anotaciones = models.IntegerField()
    faltas = models.IntegerField()
    asistencias = models.BooleanField()
