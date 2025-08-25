from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from .models import Genre, Book


def home(request: HttpRequest):
    books = Book.objects.all()
    genres = Genre.objects.all()
    context = {
        'books': books,
        'genres': genres,
    }

    return render(request, 'main/index.html', context)

def books_by_genres(request: HttpRequest, genre_id: int):
    books = Book.objects.filter(genre_id=genre_id)
    genres = Genre.objects.all()
    context = {
        'books': books,
        'genres': genres,
    }

    return render(request, 'main/index.html', context)

def book_detail(request: HttpRequest, pk: int):
    bookses = Book.objects.get(pk=pk)
    context = {
        "bookses": bookses,
    }

    return render(request, "main/detail.html", context)
