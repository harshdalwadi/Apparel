from django.shortcuts import render,redirect, get_object_or_404
from .forms import ProductForm
from django.core.mail import send_mail
from django.contrib import messages
from apparel import settings
from django.contrib.auth.decorators import login_required
from .models import Product

# Create your views here.

# def shop(request):
# 	products = Product.objects.all()
#     template = "shop.html"
#     return render(request,template,{'products':products})

def shop(request):
	products = Product.objects.all()
	template = "shop.html"
	return render(request,template,{'products':products})

@login_required
def createproduct(request):
	if request.method == 'Post':
		product_form = ProductForm(request.POST or None, request.FILES or None)
		if product_form.is_valid():
			f = product_form.save(commit=False)
			f.user = request.user
			f.save()
			messages.success(request,"Prodct Added successfully")
			return redirect('Home:Home')
		else:
			messages.error(request,"failed to add Prodct")
	else:
		product_form = ProductForm()
	template = "createproduct.html"
	return render(request,template,{'product_form':product_form})

def singleproduct(request,pk):
	product = get_object_or_404(Product, pk=pk)
	template = 'single-product.html'
	return render(request,template,{'product':product})

def myproducts(request):
	myproducts = Product.objects.filter(user__id = request.user.id)
	template = 'my_products.html'
	return render(request,template,{'products': myproducts})	

def updateproduct(request,pk):
	template = "update_product.html"
	product =  get_object_or_404(Product,pk = pk)
	form = ProductForm(request.POST or None, request.FILES or None, instance = product)
	if form.is_valid():
		form.save()
		messages.success(request,"Product is updated successfully")
		return redirect("Home:Products:myproducts")
	return render(request,template,{'product_form':form})

def deleteproduct(request,pk):
	template = "delete_product.html"
	product =  get_object_or_404(Product,pk = pk)
	if request.method == 'POST':
		product.delete()
		messages.success(request,"Product is deleted successfully")
		return redirect("Home:Products:myproducts")
	return render(request,template)

def search(request):
    template = 'products/shop.html'
    if "search" in request.GET:
        srh = request.GET["search"]
        # # p = request.GET["price"]
        prd = Product.objects.filter(name__contains=srh)  # search by product name
        # prd = Product.objects.filter(Q(name__contains=srh)|Q(category__name__contains=srh))
        # # prd = Product.objects.filter(Q(name__contains=srh) & Q(price__lt=p)) # search by product name and and pice less than use two search field in html
    return render(request,template,{'products':prd})
