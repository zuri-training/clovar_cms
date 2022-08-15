from django.db import models

# Create your models here.

class Template(models.Model):
    directory = models.CharField(max_length=20, null=None)
    template_index = models.CharField(max_length=20, default="index.html")

    def __str__ (self):
        return self.directory