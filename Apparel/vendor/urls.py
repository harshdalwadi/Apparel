from django.urls import path, include
from .views import login, signup, verification_sent, confirm_email, home, logout, reset_password, forgot_password, otp_sent, otp_verify, change_password

app_name = "Vendor"

urlpatterns = [
	path('',home,name="home"),
	path('signup/',signup,name="signup"),
	path('login/',login,name="login"),
	path('verification_sent/',verification_sent,name='verification_sent'),
	path('confirm_email/',confirm_email,name='confirm_email'),
    path('reset_password/',reset_password,name='reset_password'),
    path('logout/',logout,name='logout'),
	path('forgot_password/',forgot_password,name='forgot_password'),
	path('otp_sent',otp_sent,name='otp_sent'),
    path('otp_verify',otp_verify,name='otp_verify'),
	path('change_password/',change_password,name='change_password'),
]
