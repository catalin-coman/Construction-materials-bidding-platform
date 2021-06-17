from django.db import models

# Create your models here.

class Concrete(models.Model):
    Type = models.CharField(max_length=100)
    Diameter = models.IntegerField()
    Consistency = models.IntegerField()

    def __str__(self):
        return 'Concrete ' + self.Type + ' D' + str(self.Diameter) + ' S' + str(self.Consistency)