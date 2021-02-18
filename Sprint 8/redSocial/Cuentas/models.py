from django.db import models


# Create your models here.
class User(models.Model):
    class Meta:
        ordering = ['username']

    username = models.CharField(max_length=128, unique=True, primary_key=True)
    password = models.CharField(max_length=222, null=False)
    email = models.EmailField(max_length=180, null=False)

    def __str__(self):
        return self.username

class Followers(models.Model):
    class Meta:
        ordering = ['id_followers']

    id_followers = models.CharField(max_length=80, unique=True, primary_key=True)
    my_follows = models.IntegerField()
    my_followers = models.IntegerField()
    username = models.ForeignKey(User,max_length=128, unique=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_followers