# Generated by Django 3.1.5 on 2021-02-18 00:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Cuentas', '0004_auto_20210218_0138'),
        ('Coments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coments',
            name='username',
            field=models.ForeignKey(max_length=128, on_delete=django.db.models.deletion.CASCADE, to='Cuentas.user'),
        ),
    ]