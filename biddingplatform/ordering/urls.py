from django.urls import path
from . import views

urlpatterns = [ 
    #order form
    path('order', views.CreateOrder.as_view(), name='order-form'),
]