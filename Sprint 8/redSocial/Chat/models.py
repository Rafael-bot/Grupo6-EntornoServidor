from django.db import models

# Create your models here.

class Chat(models.Model):
    class Meta:
        ordering = ['date_text']

    id_chat = models.CharField(max_length=80, unique=True, primary_key=True)
    chat_text = models.TextField(max_length=2021)
    date_text = models.DateTimeField()
    username = models.ForeignKey("Cuentas.User", max_length=128, unique=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.chat_text