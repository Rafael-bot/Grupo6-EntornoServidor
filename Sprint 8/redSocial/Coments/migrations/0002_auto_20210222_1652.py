# Generated by Django 3.1.5 on 2021-02-22 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Coments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coments',
            name='number_likes',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
