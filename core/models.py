from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from djongo import models
import uuid
import requests
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

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = SystemAdmin()  # set your custom manager

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'auth_user'


