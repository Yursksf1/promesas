from django.core.management.base import BaseCommand
from myapp.models import Categoria

class Command(BaseCommand):
    def handle(self, *args, **options):
        print(">>> Creando categorias")
        categorias = [
         ["sub 12", "my description"],
         ["sub 13", "my description"],
         ["sub 14", "my description"],
         ["sub 15", "my description"],
         ["sub 16", "my description"],
         ["sub 17", "my description"],
         ["sub 18", "my description"],
        ]

        for categoria in categorias: 
            nombre = categoria[0]
            descripcion = categoria[1]
            print("creando categoria {} descripcion {}".format(nombre, descripcion))
            categoria_obj = Categoria(nombre=nombre, descripcion=descripcion)
            categoria_obj.save()