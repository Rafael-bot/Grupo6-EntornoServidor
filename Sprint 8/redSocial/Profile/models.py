from django.db import models


# Create your models here.
class Profile(models.Model):
    class Meta:
        ordering = ['id_profile']

    id_profile = models.CharField(max_length=80, unique=True, primary_key=True)
    biography = models.TextField(max_length=1000)
    photo = models.ImageField(upload_to='profile')
    username = models.ForeignKey("Cuentas.User", max_length=128, on_delete=models.CASCADE)
    id_posts = models.ForeignKey("Posts.Posts", max_length=80, on_delete=models.CASCADE)
    id_followers = models.ForeignKey("Cuentas.Followers", max_length=80, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_profile
