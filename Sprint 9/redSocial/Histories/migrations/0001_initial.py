# Generated by Django 3.1.6 on 2021-02-23 23:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Cuentas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Histories',
            fields=[
                ('id_history', models.CharField(max_length=80, primary_key=True, serialize=False, unique=True)),
                ('history', models.ImageField(blank=True, null=True, upload_to='history')),
                ('date_of_history', models.DateTimeField()),
                ('username', models.ForeignKey(max_length=128, on_delete=django.db.models.deletion.CASCADE, to='Cuentas.user')),
            ],
            options={
                'ordering': ['date_of_history'],
            },
        ),
    ]