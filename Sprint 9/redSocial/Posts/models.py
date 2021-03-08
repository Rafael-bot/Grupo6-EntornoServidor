from django.db import models

# Create your models here.


class Posts(models.Model):

    class Meta:
        ordering = ['post_date']

    id_posts = models.CharField(max_length=80, unique=True, primary_key=True)
    number_posts = models.IntegerField()
    number_likes = models.IntegerField(blank=True,null=True)
    photo = models.ImageField(upload_to='posts',blank=True,null=True)
    description = models.TextField(max_length=500, null=True)
    post_date = models.DateTimeField()
    public_or_private = models.BooleanField()
    username = models.ForeignKey('Cuentas.User', max_length=128,on_delete=models.CASCADE)
    id_coments = models.ForeignKey('Coments.Coments',max_length=80, on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.id_posts