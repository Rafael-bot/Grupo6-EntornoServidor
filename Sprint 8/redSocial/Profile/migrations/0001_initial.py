# Generated by Django 3.1.6 on 2021-02-23 23:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Posts', '0001_initial'),
        ('Cuentas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id_profile', models.CharField(max_length=80, primary_key=True, serialize=False, unique=True)),
                ('biography', models.TextField(max_length=1000)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='profile')),
                ('id_followers', models.ForeignKey(blank=True, max_length=80, null=True, on_delete=django.db.models.deletion.CASCADE, to='Cuentas.followers')),
                ('id_posts', models.ForeignKey(blank=True, max_length=80, null=True, on_delete=django.db.models.deletion.CASCADE, to='Posts.posts')),
                ('username', models.ForeignKey(max_length=128, on_delete=django.db.models.deletion.CASCADE, to='Cuentas.user')),
            ],
            options={
                'ordering': ['id_profile'],
            },
        ),
    ]
