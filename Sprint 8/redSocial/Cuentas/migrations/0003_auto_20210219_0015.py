# Generated by Django 3.1.6 on 2021-02-19 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cuentas', '0002_auto_20210219_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=128, primary_key=True, serialize=False, unique=True),
        ),
    ]
