from django.db import models

# Create your models here.

class Dan(models.Model):
    name = models.CharField(max_length=20)


class Duo(models.Model):
    name = models.CharField(max_length=20)
    describe = models.CharField(max_length=100)
    key = models.ForeignKey("Dan", on_delete=models.CASCADE)