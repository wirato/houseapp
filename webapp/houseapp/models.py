from django.db import models

# Create your models here.
class Housedata(models.Model):
    id = models.AutoField(primary_key=True)
    X1 = models.FloatField()
    X2 = models.FloatField()
    X3 = models.FloatField()
    X4 = models.FloatField()
    X5 = models.FloatField()
    X6 = models.FloatField()

    def __str__(self):
        return str(self.id)

class Price_of_unit_area(models.Model):
    id = models.AutoField(primary_key=True)
    Y = models.FloatField()

    def __str__(self):
        return str(self.Y)