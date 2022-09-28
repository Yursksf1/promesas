from django.contrib import admin
from myapp.models import Video, Acudiente, Pago, Jugador, Equipo, Resultado, Subscripcion, Horario_partido, Entrenamientos_jugador, Resultado, Video


@admin.register(Acudiente)
class AcudienteAdmin(admin.ModelAdmin):
    pass

@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    pass

@admin.register(Jugador)
class JugadorAdmin(admin.ModelAdmin):
    pass

@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    pass

@admin.register(Subscripcion)
class SubscripcionAdmin(admin.ModelAdmin):
    pass

@admin.register(Horario_partido)
class Horario_partidoAdmin(admin.ModelAdmin):
    pass

@admin.register(Entrenamientos_jugador)
class Entrenamientos_jugadorAdmin(admin.ModelAdmin):
    pass

@admin.register(Resultado)
class ResultadoAdmin(admin.ModelAdmin):
    pass

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    pass
