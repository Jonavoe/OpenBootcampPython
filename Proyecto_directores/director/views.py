from traceback import StackSummary
from django.shortcuts import render

from .models import Description, Genre, Movie, Author, Description

def index(request):
    movies = Movie.objects.all().get()
    genres = Genre.objects.all().get()
    authors = Author.objects.all().get()
    description = Description.objects.all().get()
    
    return render(
        request,
        'index.html',
        context={
            'movies': movies,
            'genres': genres,
            'authors': authors,
            'description': description
        }
    )
