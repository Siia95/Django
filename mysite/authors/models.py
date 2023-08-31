from django.db import models
from accounts.models import CustomUser

class Author(models.Model):
    users = models.ManyToManyField(CustomUser)
    name = models.CharField(max_length=255)
    birth_date = models.DateField()
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name


