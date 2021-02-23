# Generated by Django 3.1.6 on 2021-02-23 23:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Cuentas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coments',
            fields=[
                ('id_coments', models.CharField(max_length=80, primary_key=True, serialize=False, unique=True)),
                ('coment_text', models.TextField(max_length=2021)),
                ('date_of_coment', models.DateTimeField()),
                ('number_likes', models.IntegerField(blank=True, null=True)),
                ('username', models.ForeignKey(max_length=128, on_delete=django.db.models.deletion.CASCADE, to='Cuentas.user')),
            ],
            options={
                'ordering': ['date_of_coment'],
            },
        ),
    ]
