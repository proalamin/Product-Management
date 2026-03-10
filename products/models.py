from django.db import models


class Product(models.Model):
    STATUS_CHOICES = [
        ('Draft', 'Draft'),
        ('Approved', 'Approved'),
    ]

    product_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Draft')

    def __str__(self):
        return f"{self.product_id} - {self.name}"

    class Meta:
        ordering = ['-last_updated']
