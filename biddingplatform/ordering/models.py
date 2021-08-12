from django.db import models
from django.db.models.fields import AutoField, IntegerField, CharField, DateTimeField
from django.urls import reverse
from django.db.models.fields.related import ForeignKey
from django.db.models.deletion import CASCADE

from accounts import models as accounts_models
from concrete import models as concrete_models

# Create your models here.

class Order(models.Model):

    MOBILE_PUMP = 'MP'
    STATIONARY_PUMP = 'SP'
    NO_PUMP = 'NO'
    CONCRETE_PUMP_CHOICES = [
        (MOBILE_PUMP, 'Mobile pump'),
        (STATIONARY_PUMP, 'Stationary pump'),
        (NO_PUMP, 'No pump')
    ]

    Concrete = ForeignKey(concrete_models.Concrete, on_delete=CASCADE)
    Quantity = IntegerField(null=False)
    Concrete_pump = CharField(max_length=2, choices=CONCRETE_PUMP_CHOICES, default=NO_PUMP)
    Address = CharField(max_length=100, null=False)
    Pour_date = DateTimeField(null=False)
    Order_date = DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("concrete-home")

    def __str__(self):
        return 'Order number ' + str(self.id) + ' created on ' +str(self.Order_date) + ' by ' + ' - ' + str(self.Concrete) + ' pouring date ' + str(self.Pour_date)