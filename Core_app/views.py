from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from Core_app.models import Blog, Contact_Us
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from.forms import Contact_Uss
# Create your views here.


# services
def services(request):
    return render(request, 'Core_app/services.html')

# about


def about(request):
    return render(request, 'Core_app/about.html')


# portfolio

def portfolio(request):
    return render(request, 'Core_app/portfolio.html')

# blog


# portfolio details


def portfolio_details(request):
    return render(request, 'Core_app/portfolio_details.html')

# contact


def contact(request):
    if request.method == 'POST':
        form = Contact_Uss(request.POST)
        if form.is_valid():
            message = form.cleaned_data.get('message')
            name = form.cleaned_data.get('name')
            title = form.cleaned_data.get('title')
            email = form.cleaned_data.get('email')

            user = Contact_Us(message=message, name=name,
                              title=title, email=email)

            user.save()
            messages.success(request, 'Hey '+name +
                             ' ! We got your message. We will get back to you soon!')
            return redirect('index')

    else:
        form = Contact_Uss()
    return render(request, 'Core_app/contact.html', {
        'forms': form,
    })
