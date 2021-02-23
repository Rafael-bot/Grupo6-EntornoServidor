import os
import time

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'redSocial.settings')
import django, random as rd

from random import random

django.setup()

from Cuentas.models import User

vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
consonantes = ['b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'y', 'z',
               'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Y', 'Z']


def generar_cadena(lenght):
    if lenght <= 0:
        return False

    cadena = ''

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


def generate_number():
    return int(random() * 10 + 1)


def populate(count):
    for i in range(count):
        random_user = generar_cadena(generate_number())
        random_pasw = generar_cadena(generate_number())
        random_mail = generar_cadena(generate_number())

        User.objects.create(
            username=random_user,
            password=random_pasw,
            email=random_mail
        )


if __name__ == '__main__':
    print("inicio de la creacion de populate")
    print("por favor espere")
    start = time.strftime("%c")
    print(f'fecha y hora de inicio: {start}')
    generar_cadena(50)
    end = time.strftime("%c")
    print(f'fecha y hora de finalizacion: {end}')
