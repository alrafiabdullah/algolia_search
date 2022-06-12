from django.db import models


# Create your models here.
class Cars(models.Model):
    COLOR_CHOICES = (
        ('red', 'Red'),
        ('blue', 'Blue'),
        ('green', 'Green'),
    )

    name = models.CharField(max_length=255)
    cc = models.PositiveSmallIntegerField()
    color = models.CharField(max_length=255, choices=COLOR_CHOICES)
    price = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name
