from django.contrib import admin
from myapp.models import Acudiente, Pago, Jugador, Equipo, Resultado, Subscripcion, Horario_partido, Entrenamientos_jugador, Resultado


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
class SubscripcionAdmin(admin.ModelAdmin):
    pass

@admin.register(Entrenamientos_jugador)
class SubscripcionAdmin(admin.ModelAdmin):
    pass

@admin.register(Resultado)
class SubscripcionAdmin(admin.ModelAdmin):
    pass
