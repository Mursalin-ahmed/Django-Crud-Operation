from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=20)
    roll = models.PositiveIntegerField()
    img = models.ImageField(upload_to='images/',default='def.png',null=True,blank=True)


    def __str__(self):
        return self.name