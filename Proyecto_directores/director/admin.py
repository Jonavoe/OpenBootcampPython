import imp
from re import M
from django.contrib import admin

from .models import Author, Movie, Genre, Description

admin.site.register(Author)
admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Description)




