from django.contrib.gis.db import models
#Create your models here.

class polygon(models.Model):
    description=models.CharField(max_length=100)
    coordinates=models.PolygonField(srid=4326)

def __str__(self):
    return self.name


class line(models.Model):
    description=models.CharField(max_length=100)
    coordinates=models.LineStringField(srid=4326)

def __str__(self):
    return self.name


class point(models.Model):
    description=models.CharField(max_length=100)
    coordinates=models.PointField(srid=4326)

def __str__(self):
    return self.name

class Image(models.Model):
    description=models.CharField(max_length=256)
    image=models.ImageField(upload_to='static/categorias')

    def __str__(self):
        return self.description

