from django.urls import path

from . import views

urlpatterns = [

    # homepage
    path ('', views.concrete, name='concrete-home'),

]
