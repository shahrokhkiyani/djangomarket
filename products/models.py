from django.db import models


class Product(models.Model):

    ACTIVE_CHOICES = (
        ('avb', 'Available'),
        ('una', 'Unavailable')
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField()
    active = models.CharField(max_length=3, choices=ACTIVE_CHOICES)
    # cover = models.ImageField()

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
