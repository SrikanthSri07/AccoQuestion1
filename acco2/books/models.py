from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)

    def _str_(self):
        return f"{self.title} by {self.author}"