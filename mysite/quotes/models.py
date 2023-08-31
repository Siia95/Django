from django.db import models
from authors.models import Author

class Quote(models.Model):
    text = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='quotes')

    def __str__(self):
        return self.text

