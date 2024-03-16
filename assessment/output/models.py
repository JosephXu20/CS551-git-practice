from django.db import models
from django.conf import settings

# Create your models here.

class Data(models.Model):
    id = models.AutoField(primary_key=True)
    countryName = models.TextField()
    year1 = models.IntegerField()
    year2 = models.IntegerField()
    year3 = models.IntegerField()
    year4 = models.IntegerField()
    year5 = models.IntegerField()
    year6 = models.IntegerField()

    def __str__(self):
        return self.id, self.countryName, self.year1, self.year2, self.year3, self.year4, self.year5, self.year6

class MetadataCountries(models.Model):
    id = models.AutoField(primary_key=True)
    region = models.TextField()
    incomeGroup = models.TextField()
    specialNotes = models.TextField()
    tableName = models.TextField()

    def __str__(self):
        return self.id, self.region, self.incomeGroup, self.specialNotes, self.tableName