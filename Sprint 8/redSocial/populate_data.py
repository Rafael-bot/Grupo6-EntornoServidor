import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'redSocial.settings')

import django

django.setup()

from Cuentas.models import Cuentas, Chat

from faker import Faker

fakegen = Faker()

def populate(n=5):
    for entry in range(n):
        fake_profile = fakegen.profile()
        fake_username = fakegen.username()
        fake_email = fakegen.email()
        fake_password = fakegen.password()
        fake_tlfn = fakegen.tlfn()
        fake_biography = fakegen.biography()

        #Nueva entrada de datos

        user = Cuentas.object.get_or_create(profile = fake_profile, username = fake_username, password = fake_password, email = fake_email, biography = fake_biography)[0]

if __name__ == '__main__':
    print("RELLENANDO BASE DE DATOS")
    populate(20)
    print('COMPLETADO!')
    




