from django.urls import path, include
from .views import contact,profile,home

app_name = "Home"

urlpatterns = [
	path('',home,name="Home"),
	path('contact/',contact,name="contact"),
	path('profile/',profile,name="profile"),
	path('products/',include('products.urls')),
]
