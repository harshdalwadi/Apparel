from django.urls import path, include
from .views import shop, createproduct, singleproduct, myproducts, updateproduct, deleteproduct, search

app_name = "Products"

urlpatterns = [
	path("shop/",shop,name="shop"),
	path("createproduct/",createproduct,name="createproduct"),
	path("singleproduct/<int:pk>/",singleproduct,name="singleproduct"),
	path("myproducts/",myproducts,name="myproducts"),
	path("updateproduct/<int:pk>/",updateproduct,name="updateproduct"),
	path("deleteproduct/<int:pk>/",deleteproduct,name="deleteproduct"),
	path('cart/',include('cart.urls')),
	path('search/',search,name="search")
]