from django.db import models

# Create your models here.


class Foto(models.Model):

    class Meta:
        ordering = ['cat']

    foto = models.ImageField(upload_to='posts')
    descripcion = models.TextField(max_length=500, null=True)
    cat = models.CharField(max_length=12)
    username = models.ForeignKey('Cuentas.Cuentas', max_length=128,on_delete=models.CASCADE)
    comment_code = models.CharField(max_length=10, primary_key=True)

    def __str__(self):
        return self.cat


class Coments(models.Model):

    class Meta:
        ordering = ['date']

    text = models.CharField(max_length=2021)
    date = models.DateTimeField()
    username = models.ForeignKey('Cuentas.Cuentas', max_length=128,on_delete=models.CASCADE)
    comment_code = models.ForeignKey(Foto,max_length=10, primary_key=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
