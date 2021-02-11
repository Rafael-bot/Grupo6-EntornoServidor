from django.db import models


# Create your models here.
class Cuentas(models.Model):
    class Meta:
        ordering = ['username']

    profile = models.ImageField(upload_to='profile', null=True)
    username = models.CharField(max_length=128, unique=True, primary_key=True)
    password = models.CharField(max_length=222, null=False)
    email = models.EmailField(max_length=180, blank=True, null=True)
    tlfn = models.CharField(max_length=12, null=True)
    biography = models.TextField(max_length=1200, blank=True, null=True)

    def __str__(self):
        return self.username


class Chat(models.Model):
    class Meta:
        ordering = ['date']

    chatText = models.TextField(max_length=2021)
    date = models.DateTimeField()
    username = models.ForeignKey(Cuentas, max_length=128, on_delete=models.CASCADE)

    def __str__(self):
        return self.chatText
