from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from .models import Address
from .forms import AddressForm
from django.contrib import messages

class HomePageView(ListView):
    model = Address
    template_name='home.html'
    context_object_name = 'addresses'

class AddressPageView(TemplateView):
    template_name='add_address.html'  

def add_address(request):
    if request.method == 'POST':
        form = AddressForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, ('Address Has Been Added'))
            return redirect('home')
        else:
            messages.success(request, ('Seems like there was an error'))
            return render(request,'add_address.html')
    else:
        return render(request, 'add_address.html', {})
# Create your views here.

def edit_address(request, list_id):
    if request.method == 'POST':
        current_address = Address.objects.get(pk=list_id)
        form = AddressForm(request.POST or None, instance=current_address)
        if form.is_valid():
            form.save()
            messages.success(request, ('Address Has Been Edited'))
            return redirect('home')
        else:
            messages.success(request, ('Seems like there was an error'))
            return render(request,'edit.html')
    else:
        get_address = Address.objects.get(pk=list_id)
        return render(request, 'edit.html', {'get_address': get_address})

def delete_address(request, list_id):
    if request.method == 'POST':
        current_address = Address.objects.get(pk=list_id)
        current_address.delete()
        messages.success(request, ('Address Has Been Deleted'))
        return redirect('home')
    else:
        messages.success(request, ('Nothing to see here'))
        return redirect('home')