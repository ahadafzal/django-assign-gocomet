from django.db import models
from django.utils import timezone

PRODUCT_CHOICES = (
        ('1', 'ORDER PLACE'),
        ('2', 'ON THE WAY'),
        ('3', 'DELIVERED'),
        ('4', 'RETURNED'),
        ('5', 'PROCESS COMPLETE'),
    )

class Product(models.Model):
	product_name = models.CharField(max_length=20, blank=False)
	product_image = models.ImageField(upload_to='', blank=True)
	product_price = models.DecimalField(max_digits=10, decimal_places=2)
	product_chosen = models.CharField(max_length=20, choices=PRODUCT_CHOICES)
	product_date = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return f'Product {self.product_name}'
		
	def update(self, **kwargs):
		if self._state.adding:
			raise self.DoesNotExist
		for field, value in kwargs.items():
			setattr(self, field, value)
		self.save(update_fields=kwargs.keys())

	class Meta:
		ordering = ('-product_date',)