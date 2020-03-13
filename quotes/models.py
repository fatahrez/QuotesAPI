from django.db import models


# Create your models here.
class Quotes(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=50)
    image_inspiration = models.ImageField()

    def __str__(self):
        return self.author