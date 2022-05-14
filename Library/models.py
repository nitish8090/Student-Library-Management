from django.db import models
from StudentLibrarian.models import ObjectLog, Student, Librarian


class Book(ObjectLog):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    quantity = models.IntegerField(default=0)
    quantity_issued = models.IntegerField(default=0)


class BookIssue(ObjectLog):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, to_field='serial')
    issued_by = models.ForeignKey(Librarian, on_delete=models.CASCADE)
    is_returned = models.BooleanField(default=False)
