from django.urls import path
from .import views

app_name = 'app_core'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('portfolio_details/', views.portfolio_details, name='portfolio_details'),
    path('contact/', views.contact, name='contact'),
]
