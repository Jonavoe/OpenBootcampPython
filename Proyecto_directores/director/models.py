from django.db import models
from django.urls import reverse

class Genre(models.Model):
    
    name = models.CharField(max_length=200, help_text="Ingrese el nombre del género (p. ej. Ciencia Ficción, Terror etc.)")

    def __str__(self):
        
        return self.name
    
class Description(models.Model):
    
    name = models.TextField(max_length=200, help_text="Descripcion de la pelicula.)")

    def __str__(self):
        
        return self.name
    
class Movie(models.Model):
    title = models.CharField(max_length=32)
    author = models.ForeignKey('Author',on_delete=models.SET_NULL, null= True)
    sumary = models.TextField(max_length=100, help_text="Descripcion de la Pelicula")
    genre = models.ManyToManyField(Genre)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("movie_detail", args=[str(self.id)])
    
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)
    
    def get_absolute_url(self):
        return reverse("author_detail", args=[str(self.id)])
    
    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)