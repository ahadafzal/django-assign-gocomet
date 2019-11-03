from django import forms
from .models import Product

class CreateProductForm(forms.ModelForm):

	class Meta:
		model = Product
		fields = ['product_name', 'product_image', 'product_price','product_date']

