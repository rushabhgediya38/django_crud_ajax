from django.db import models


# Create your models here.


class crud_post(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Post(models.Model):
    name = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=100)
    image = models.FileField(upload_to='image/')

    def __str__(self):
        return self.name

