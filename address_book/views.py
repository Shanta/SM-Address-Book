from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name='home.html'

class AddressPageView(TemplateView):
    template_name='add_address.html'  

# Create your views here.
