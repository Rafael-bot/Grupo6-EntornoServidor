import os
import time

from django.utils.timezone import now

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'redSocial.settings')
import django, random as rd

from random import random

django.setup()

from Cuentas.models import User, Followers
from Chat.models import Chat
from Coments.models import Coments
from Histories.models import Histories
from Posts.models import Posts
from Profile.models import Profile

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

def generate_number_posts():
    return int(random() * 2000 + 1)


def generate_number_text():
    return int(random() * 100 + 1)

def generate_boolean_posts(num):
    if num%2==0:
        return True
    else:
        return False

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
        populate_chats(random_user)
        populate_coments(random_user, i)
        populate_histories(random_user)
        populate_profiles(random_user)


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


def populate_chats(user):
    random_id_chat = generar_cadena(generate_number_id())
    random_chat_text = generar_cadena(generate_number_text())
    random_date_text = now()
    random_username = user

    dato = Chat.objects.create(
        id_chat=random_id_chat,
        chat_text=random_chat_text,
        date_text=random_date_text,
        username_id=random_username
    )
    dato.save()


def populate_coments(user, num):
    random_id_coments = generar_cadena(generate_number_id())
    random_coment_text = generar_cadena(generate_number_text())
    random_date_of_coment = now()
    random_number_likes = generate_number_follows()
    random_username = user

    dato = Coments.objects.create(
        id_coments=random_id_coments,
        coment_text=random_coment_text,
        date_of_coment=random_date_of_coment,
        number_likes=random_number_likes,
        username_id=random_username
    )
    dato.save()

    populate_posts(random_id_coments, user, num)

def populate_posts(id_coments, user, num):
    random_id_posts = generar_cadena(generate_number_id())
    random_number_posts = generate_number_posts()
    random_number_likes = generate_number_posts()
    random_description = generar_cadena(generate_number_text())
    random_post_date = now()
    random_public_or_private = generate_boolean_posts(num)
    random_username = user
    random_id_coments = id_coments

    dato = Posts.objects.create(
        id_posts=random_id_posts,
        number_posts=random_number_posts,
        number_likes=random_number_likes,
        photo=None,
        description=random_description,
        post_date=random_post_date,
        public_or_private=random_public_or_private,
        username_id=random_username,
        id_coments_id=random_id_coments
    )
    dato.save()


def populate_histories(user):
    random_id_history = generar_cadena(generate_number_id())
    random_date_of_history = now()
    random_username = user

    dato = Histories.objects.create(
        id_history=random_id_history,
        history=None,
        date_of_history=random_date_of_history,
        username_id=random_username
    )
    dato.save()

def populate_profiles(user):
    random_id_profile = generar_cadena(generate_number_id())
    random_biography = generar_cadena(generate_number_text())
    random_username = user

    dato = Profile.objects.create(
        id_profile=random_id_profile,
        biography=random_biography,
        photo=None,
        username_id=random_username,
        id_posts_id=None,
        id_followers_id=None
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
