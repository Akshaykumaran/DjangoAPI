from django.db import models
from datetime import datetime
# Create your models here.

class Blog(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    books = models.CharField(max_length=80)
    author = models.CharField(max_length=50)
    created_at = models.DateTimeField(default = datetime.now)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField()
    father = models.CharField(max_length=80)
    college = models.CharField(max_length=80)

    def __str__(self):
        return self.name
    
class Books(models.Model):
    name = models.CharField(max_length=80)
    author = models.CharField(max_length=80)
    read_by = models.CharField(max_length=80)

    def __str__(self):
        return self.read_by
    