from django.shortcuts import render, redirect
from .models import Product
from .forms import CreateProductForm
from django.contrib import messages


#HOMEPAGE VIEW
def homepage(request):

	products = Product.objects.all()

	if request.method == 'POST':
		form = CreateProductForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, 'The product was successfully saved!')
			return redirect('homepage')
		else:
			messages.error(request, 'The product was not saved due to validation error!')
			return redirect('homepage')
	else:
		form = CreateProductForm()


	context = {
		'products_order_placed':products.filter(product_chosen=1),
		'products_on_the_way':products.filter(product_chosen=2),
		'products_delivered':products.filter(product_chosen=3),
		'products_returned':products.filter(product_chosen=4),
		'products_proceed_completed':products.filter(product_chosen=5),
		'form': form
	}

	return render(request, 'products/products_list.html', context)


#SIMPLE AJAX FOR CHANGING CATEGORIES
def change_product_class(request):
	id_ = request.GET.get('prodId');
	categoryId = request.GET.get('categoryId')
	product = Product.objects.get(id=id_)
	product.update(product_chosen=categoryId)