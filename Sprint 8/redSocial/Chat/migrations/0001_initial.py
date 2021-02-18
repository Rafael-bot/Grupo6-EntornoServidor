# Generated by Django 3.1.5 on 2021-02-18 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id_chat', models.CharField(max_length=80, primary_key=True, serialize=False, unique=True)),
                ('chat_text', models.TextField(max_length=2021)),
                ('date_text', models.DateTimeField()),
            ],
            options={
                'ordering': ['date_text'],
            },
        ),
    ]