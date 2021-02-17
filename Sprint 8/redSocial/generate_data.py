import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'redSocial.settings')

import django

django.setup()

from Cuentas.models import Cuentas
from faker import Faker

fakegen = Faker()


def generate(n=6):
    for entry in range(n):
        fake_profile = fakegen.profile()
        fake_username = fakegen.name()
        fake_password = fakegen.text()
        fake_email = fakegen.email()
        fake_tlfn = fakegen.phone_number()
        fake_biography = fakegen.text()

        cuentas = Cuentas.objects.get_or_create(profile=fake_profile, username=fake_username, password=fake_password,
                                                email=fake_email, tlfn=fake_tlfn, biography=fake_biography)[0]


if __name__ == '__main__':
    print("RELLENANDO BASE DE DATOS")
    generate(11)
    print('COMPLETADO!')
