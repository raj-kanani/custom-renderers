from django.db import models


# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField()
    address = models.CharField(max_length=120)


class Category(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Image(models.Model):
    options = (
        ('active', 'Active'),
        ('disactive', 'Disactive')
    )
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=120)
    alt = models.TextField(null=True)
    slug = models.SlugField(unique=True)
    status = models.CharField(max_length=12, choices=options, default='active')
