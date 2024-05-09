from django.db import models
import os


# Create your models here.
class Pests(models.Model):
    image=models.ImageField(upload_to='app/static/pestssave')

    def filename(self):
        return os.path.basename(self.image.name)