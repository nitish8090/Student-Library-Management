from django.db import models
from StudentLibrarian.models import ObjectLog


class Book(ObjectLog):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
