from django.db import models

# Create your models here.

class Snippet(models.Model):
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=30)
    lineous = models.BooleanField
    language = models.CharField(max_length=30)
    style = models.CharField(max_length=30)

    def __str__(self):
        return self.title
