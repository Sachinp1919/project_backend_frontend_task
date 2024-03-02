from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core import validators

class Person(models.Model):

    GENDER = [
        ('male', 'male'),
        ('female', 'female'),
        ('other', 'other')
    ]


    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=20, choices=GENDER)
    contact = PhoneNumberField(region='IN')
    address = models.TextField()
    city = models.CharField(max_length=20)
    pin_code = models.IntegerField()
    profile_pic = models.ImageField(upload_to='profile_pc')