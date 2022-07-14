from django.contrib import admin
from myapp.models import Acudiente, Pago, Jugador, Equipo, Subscripcion


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