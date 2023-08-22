from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
import uuid
import json
#import pandas as pd
import datetime

"""
headers = { 'AccountKey' : 'ZSRd6ixqSy+V+GnHTV7/iQ==',
             'accept' : 'application/json'} 
"""

class SystemAdmin(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        if not email:
            raise ValueError('The Email field must be set')

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)  # superusers are staff

        return self.create_user(username, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # add this
    is_superuser = models.BooleanField(default=False)  # add this

    homeAddress = models.CharField(max_length=255, default='', blank=True)
    workAddress = models.CharField(max_length=255, default='', blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = SystemAdmin()  # set your custom manager

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'auth_user'


# Traffic Jam
class TrafficJam(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField()
    time = models.TimeField()
    message = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"Traffic Jam, datetime: {self.date}, {self.time}, message: {self.message}"

    def create_traffic_jam(self, date, time, message, location, *args, **kwargs):
        self.message = message
        self.date = date
        self.time = time
        self.location = location
        super().save(*args, **kwargs)

    @classmethod
    def traffic_jam_all(cls):
        return cls.objects.all()

    def update_traffic_jam(self, date, time, message, location, *args, **kwargs):
        if date is not None:
            self.date = date
        if time is not None:
            self.time = time
        if message is not None:
            self.message = message
        if location is not None:
            self.location = location
        super().save(*args, **kwargs)

    def delete_traffic_jam(self, *args, **kwargs):
        super(TrafficJam, self).delete(*args, **kwargs)

    @classmethod
    def search_traffic_jam(cls, keyword):
        return cls.objects.filter(message__icontains=keyword)

    def get_traffic_jam(self, id):
        return TrafficJam.objects.get(id=id)


# Traffic Accident
class RoadAccident(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField()
    time = models.TimeField()
    message = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"Road Accident, datetime: {self.date}, {self.time}, message: {self.message}"

    def create_road_accident(self, date, time, message, location, *args, **kwargs):
        self.message = message
        self.date = date
        self.time = time
        self.location = location
        super().save(*args, **kwargs)

    @classmethod
    def road_accident_all(cls):
        return cls.objects.all()

    def update_road_accident(self, date, time, message, location, *args, **kwargs):
        if date is not None:
            self.date = date
        if time is not None:
            self.time = time
        if message is not None:
            self.message = message
        if location is not None:
            self.location = location
        super().save(*args, **kwargs)

    def delete_road_accident(self, *args, **kwargs):
        super(RoadAccident, self).delete(*args, **kwargs)

    @classmethod
    def search_road_accident(cls, keyword):
        return cls.objects.filter(message__icontains=keyword)

    def get_road_accident(self, id):
        return RoadAccident.objects.get(id=id)



# Traffic Closure
class RoadClosure(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField()
    time = models.TimeField()
    message = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"Road Closure, datetime: {self.date, self.time}, message: {self.message}"

    def create_road_closure(self, date, time, message, location, *args, **kwargs):
        self.message = message
        self.date = date
        self.time = time
        self.location = location
        super().save(*args, **kwargs)

    @classmethod
    def road_closure_all(cls):
        return cls.objects.all()

    def update_road_closure(self, date, time, message, location, *args, **kwargs):
        if date is not None:
            self.date = date
        if time is not None:
            self.time = time
        if message is not None:
            self.message = message
        if location is not None:
            self.location = location
        super().save(*args, **kwargs)

    def delete_road_closure(self, *args, **kwargs):
        super(RoadClosure, self).delete(*args, **kwargs)

    @classmethod
    def search_road_closure(cls, keyword):
        return cls.objects.filter(message__icontains=keyword)

    def get_road_closure(self, id):
        return RoadClosure.objects.get(id=id)



