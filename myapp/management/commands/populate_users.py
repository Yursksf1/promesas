from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from myapp.models import Jugador


class Command(BaseCommand):
    def handle(self, *args, **options):
        print(">>> Creando usuarios")

        lista_de_usuarios = [
               {
                'username': "player_5",
                'first_name': "Valerie",
                'last_name': "Arismendy",
                'genero':"Femenino",
                'altura':170,
                'password': "PA$W0RD",
                'role': "SUPER_ADMIN"
                }, {
                'username': "player_4",
                'first_name': "Valerie",
                'last_name': "Arismendy",
                 'genero':"Femenino",
                'altura':170,
                'password': "PA$W0RD",
                'role': "SUPER_ADMIN"
                }
             ]

        for usuario in lista_de_usuarios:
            print("voy a crear el usuario: {}".format(usuario.get("username")))
        

            user_object = User(username=usuario['username'], email=usuario['username'], first_name=usuario['first_name'],
                                   last_name=usuario['last_name'])
            user_object.set_password(usuario['password'])
            user_object.save()
            player_object = Jugador(altura=usuario['altura'],genero=usuario['genero'],user=user_object)
            player_object.save()




