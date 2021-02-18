from django.db import models

# Create your models here.

class Coments(models.Model):
    class Meta:
        ordering = ['date_of_coment']

    id_coments = models.CharField(max_length=80, unique=True, primary_key=True)
    coment_text = models.TextField(max_length=2021)
    date_of_coment = models.DateTimeField()
    number_likes = models.IntegerField(max_length=12)
    username = models.ForeignKey('Cuentas.User', max_length=128, unique=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.coment_text