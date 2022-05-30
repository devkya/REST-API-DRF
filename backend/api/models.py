from django.db import models

# Create your models here.
class Species(models.Model):
    name = models.CharField(max_length=100)
    classification = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Person(models.Model):
    name = models.CharField(max_length=100)
    birth_year = models.DateField()
    EYE_STATUS = (
        ('b', 'black'),
        ('y', 'yellow'),
        ('g', 'green'),
        ('r', 'red'),
    )
    eye_color = models.CharField(max_length=1, 
                                 choices=EYE_STATUS, 
                                 blank=False, 
                                 help_text='r : red, y : yello, b : black, g : green')
    species = models.ForeignKey(Species, on_delete=models.CASCADE)