from django.urls import path
from . import views
from .views import RegisterView

urlpatterns = [
    path('', views.accounts, name='myaccount'),
    path('register/', RegisterView.as_view(), name='register'),
]