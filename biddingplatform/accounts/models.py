from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import CharField

# Create your models here.

class CustomUserModel(AbstractUser):
    
    CLIENT= 'BU'
    SELLER= 'SL'
    USER_TYPE_CHOICES= [ 
        (CLIENT, 'Buyer'),
        (SELLER, 'Seller'),
    ]    
    User_type = CharField(max_length=2, choices=USER_TYPE_CHOICES, default=CLIENT)

    def __str__(self):
        return self.username