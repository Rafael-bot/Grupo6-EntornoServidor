import os
import time

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'redSocial.settings')
import django, random as rd

from random import random

django.setup()

from Cuentas.models import User, Followers

vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
consonantes = ['b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'y', 'z',
               'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Y', 'Z']


def generar_cadena(lenght):
    cadena = ''

    if lenght <= 0:
        return False
    else:
        for i in range(lenght):
            decision = rd.choice(('consonantes', 'vocales'))

            if cadena[-1:].lower() in vocales:
                decision = 'consonantes'
            if cadena[-1:].lower() in consonantes:
                decision = 'vocales'

            if decision == 'consonantes':
                op_letra = rd.choice(consonantes)
            else:
                op_letra = rd.choice(vocales)

            if cadena == '':
                cadena += op_letra.upper()
            else:
                cadena += op_letra
    return cadena

def generate_number_user():
    return int(random() * 10 + 1)

def generate_number_id():
    return int(random() * 12 + 1)

def generate_number_follows():
    return int(random() * 1000 + 1)

def populate_user(count):
    for i in range(count):
        random_user = generar_cadena(generate_number_user())
        random_passw = generar_cadena(generate_number_user())
        random_mail = generar_cadena(generate_number_user())

        dato = User.objects.create(
            username=random_user,
            password=random_passw,
            email=random_mail + '@gmail.com'
        )
        dato.save()

        populate_followers(random_user)

def populate_followers(user):
    random_id_followers = generar_cadena(generate_number_id())
    random_my_follows = generate_number_follows()
    random_my_followers = generate_number_follows()
    random_username = user

    dato = Followers.objects.create(
        id_followers=random_id_followers,
        my_follows=random_my_follows,
        my_followers=random_my_followers,
        username_id=random_username
    )
    dato.save()

if __name__ == '__main__':
    print("inicio de la creacion de los datos")
    print("por favor espere")
    start = time.strftime("%c")
    print(f'fecha y hora de inicio: {start}')
    populate_user(10)
    end = time.strftime("%c")
    print(f'fecha y hora de finalizacion: {end}')
