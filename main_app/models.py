from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Author(models.Model):
    full_name = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.full_name}"

class Note(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=10000)
    tags = ArrayField(models.CharField(max_length=20), blank=True)
    author =  models.ForeignKey(Author, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'"{self.title}" created by {self.author}'
