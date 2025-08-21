from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    published_year = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return self.title