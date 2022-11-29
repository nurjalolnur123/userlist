from django.db import models

# Create your models here.

class Peoples(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=5)

    
    def __str__(self):
        return self.name