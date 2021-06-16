from django.contrib.auth.models import User
from django.db.models.fields import AutoField, CharField, DateTimeField, IntegerField
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from django.urls import reverse


# Create your models here.


class TypesOfConcrete(models.Model):
    Type = models.CharField(max_length=100)
    Diameter = models.IntegerField()
    Consistency = models.IntegerField()

    def __str__(self):
        return 'Concrete ' + self.Type + ' D' + str(self.Diameter) + ' S' + str(self.Consistency)

class Order(models.Model):

    MOBILE_PUMP = 'MP'
    STATIONARY_PUMP = 'SP'
    NO_PUMP = 'NO'
    CONCRETE_PUMP_CHOICES = [
        (MOBILE_PUMP, 'Mobile pump'),
        (STATIONARY_PUMP, 'Stationary pump'),
        (NO_PUMP, 'No pump')
    ]

    Buyer = CharField
    Concrete = ForeignKey(TypesOfConcrete, on_delete=CASCADE)
    Quantity = IntegerField(null=False)
    Concrete_pump = CharField(max_length=2, choices=CONCRETE_PUMP_CHOICES, default=NO_PUMP)
    Address = CharField(max_length=100, null=False)
    Pour_date = DateTimeField(null=False)
    Customer_type = CharField(max_length=20)
    Payment = CharField(max_length=20)
    Order_status = CharField(max_length=20)

    def get_absolute_url(self):
        return reverse("concrete:home", kwargs={"pk": self.pk})

    def __str__(self):
        return 'Order number ' + str(self.id) + ' by ' + str(self.Buyer) + ' - ' + str(self.Concrete) + ' on date ' + str(self.Pour_date)