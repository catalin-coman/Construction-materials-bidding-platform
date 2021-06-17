from django.shortcuts import render
from django.urls.base import reverse_lazy
from .models import Order
from django.views.generic import CreateView, UpdateView, DeleteView

# Create your views here.

class CreateOrder(CreateView):
    model = Order
    fields = ['Concrete', 'Quantity', 'Concrete_pump', 'Address', 'Pour_date']

class UpdateOrder(UpdateView):
    model = Order
    fields = ['Concrete', 'Quantity', 'Concrete_pump', 'Address', 'Pour_date']

class DeleteOrder(DeleteView):
    model = Order
    success_url = reverse_lazy('concrete:home')