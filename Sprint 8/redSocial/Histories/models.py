from django.db import models

# Create your models here.
class Histories(models.Model):
    class Meta:
        ordering = ['date_of_history']

    id_history = models.CharField(max_length=80, unique=True, primary_key=True)
    history = models.ImageField(upload_to='history')
    date_of_history = models.DateTimeField()
    username = models.ForeignKey("Cuentas.User", max_length=128, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_history