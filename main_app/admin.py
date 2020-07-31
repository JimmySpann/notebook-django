from django.contrib import admin
from .models import Author, Note

# Register your models here.
admin.site.register(Author)
admin.site.register(Note)