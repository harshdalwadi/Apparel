from django.shortcuts import render, redirect
from .forms import Contact,UserForm,ProfileForm
from django.core.mail import send_mail
from django.contrib import messages
from apparel import settings

# Create your views here.
def home(request):
	Template = "index.html"
	return render(request,Template,{})

def contact(request):
	cont = "contact.html"
	return render(request,cont,{})

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST or None)
        if form.is_valid():
            contact_name = form.cleaned_data['name']
            contact_email = form.cleaned_data['email']
            sub = form.cleaned_data['subject']
            content = form.cleaned_data['message']
            print(contact_name)
            form.save()
            subject = 'Hello ' + contact_name + ' from apparel!'
            message = 'Stay Connected. We would love to hear you!'
            email_from = settings.EMAIL_HOST_USER
            email_to = [contact_email, ]
            send_mail(subject, message, email_from, email_to)
            messages.success(request, 'Form submitted successfully.')
            return redirect('Home:Home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = ContactForm()
    template = 'contact.html'
    return render(request, template, {'form': form})

def profile(request):
    template = 'profile.html'
    if request.method == 'POST':
        user_form = UserForm(request.POST or None, request.FILES or None, instance=request.user)
        profile_form = ProfileForm(request.POST or None, request.FILES or None, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Your Profile is Updated Successfully..")
            return redirect('Home:Home')
        else:
            messages.error(request, 'Please Correct the error below')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, template, {'user_form': user_form,
                                      'profile_form': profile_form})
