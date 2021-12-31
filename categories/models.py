from django.db import models
from django.db.models.fields import CharField


class Category(models.Model):
    title = CharField(max_length=100)
    image = models.ImageField(upload_to='categories')

    def __str__(self):
        return self.title
