from django.db import models
from django.conf import settings


class ObjectLog(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    create_by = models.CharField(max_length=50)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.CharField(max_length=50, default='UnModified')

    class Meta:
        abstract = True


class Student(ObjectLog):
    id = models.AutoField(primary_key=True)
    serial = models.CharField(max_length=20, unique=True)
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    full_name = models.CharField(max_length=100)

    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    standard = models.CharField(max_length=10, null=True, blank=True)
    section = models.CharField(max_length=10, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.full_name = f"{self.f_name} {self.l_name}"
        super(Student, self).save(*args, **kwargs)


class Librarian(ObjectLog):
    id = models.AutoField(primary_key=True)
    employee_code = models.CharField(max_length=20, unique=True)

    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    full_name = models.CharField(max_length=100)

    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.full_name = f"{self.f_name} {self.l_name}"
        super(Librarian, self).save(*args, **kwargs)
