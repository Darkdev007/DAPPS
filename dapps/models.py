from django.db import models

class Crypto(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to ='images_uploaded', default= 'image.jpg')

    def __str__(self):
        return self.name