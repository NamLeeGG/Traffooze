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
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=20)
    message = models.CharField(max_length=100)

    def __str__(self):
        return f"Traffic Jam, datetime: {self.date, self.time}, message: {self.message}"

    def create_traffic_jam(self, date, time, message, *args, **kwargs):
        self.message = message
        self.date = date
        self.time = time
        super().save(*args, **kwargs)

    @classmethod
    def traffic_jam_all(cls):
        return cls.objects.all()

    def update_traffic_jam(self, date, time, message, *args, **kwargs):
        if date is not None:
            self.date = date
        if time is not None:
            self.time = time
        if message is not None:
            self.message = message
        super().save(*args, **kwargs)

    def delete_traffic_jam(self, *args, **kwargs):
        super(TrafficJam, self).delete(*args, **kwargs)

    def search_traffic_jam(cls, keyword):
        return cls.objects.filter(message__icontains=keyword)

    def get_traffic_jam(self, message):
        return TrafficJam.objects.get(message=message)

# Traffic Accident
class TrafficAccident(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=20)
    message = models.CharField(max_length=100)

    def __str__(self):
        return f"Traffic Accident, datetime: {self.date, self.time}, message: {self.message}"

    def create_traffic_accident(self, date, time, message, *args, **kwargs):
        self.message = message
        self.date = date
        self.time = time
        super().save(*args, **kwargs)

    @classmethod
    def traffic_accident_all(cls):
        return cls.objects.all()

    def update_accident_accident(self, date, time, message, *args, **kwargs):
        if date is not None:
            self.date = date
        if time is not None:
            self.time = time
        if message is not None:
            self.message = message
        super().save(*args, **kwargs)

    def delete_traffic_accident(self, *args, **kwargs):
        super(TrafficAccident, self).delete(*args, **kwargs)

    def search_traffic_accident(cls, keyword):
        return cls.objects.filter(message__icontains=keyword)

    def get_traffic_accident(self, message):
        return TrafficAccident.objects.get(message=message)

"""
class TrafficJam(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=20)
    message = models.CharField(max_length=100)

    def __str__(self):
        return f"Traffic Jam, datetime : {self.date, self.time}, message: {self.message}"

    def create_traffic_jam(self, date, time, message, *args, **kwargs):
        self.message = message
        self.date = date
        self.time = time
        super().save(*args, **kwargs)

    def update_traffic_jam(self, date, time, message, *args, **kwargs):
        if message is not None:
            self.message = message
        if date is not None:
            self.date = date
        if time is not None:
            self.time = time

        super().save(*args, **kwargs)

    def delete_traffic_jam(self, *args, **kwargs):
        super(TrafficJam, self).delete(*args, **kwargs)

    def get_traffic_jam(self, message):
        return TrafficJam.objects.get(message=message)

    @classmethod
    def search_traffic_jams(cls, keyword):
        return cls.objects.filter(message__icontains=keyword)

    @classmethod
    def trafficjamall(cls):
        return cls.objects.all()

    @classmethod
    def get_live_traffic_jam(cls):

        response = requests.get('http://datamall2.mytransport.sg/ltaodataservice/TrafficIncidents', headers=headers)

        data = response.json()["value"]
        data = json.dumps([obj for obj in data])
        df = pd.read_json(data)
        df[['Date', 'Time']] = df['Message'].str.extract(r'\((.*?)\)(.*?) ')
        df['Message'] = df['Message'].str.replace(r'\((.*?)\)(.*?) ', '', regex=True)
        current_year = datetime.datetime.now().year
        df['Date'] = df['Date'] + '/' + str(current_year)

        jam = df.loc[df['Type'] == "Heavy Traffic"]

        traffic_jams = []

        for index, row in jam.iterrows():
            date = row["Date"]
            time = row["Time"]
            message = row['Message']
            # location = row["Latitude"] + row["Longitude"]
            # or use OneMap API to reverse geocode the lat long to an address, but OneMap hasn't replied me yet

            traffic_jam = cls(date=date, time=time, message=message)
            traffic_jam.save()
            traffic_jams.append(traffic_jam)

        return traffic_jams

class TrafficClosure(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=20)
    message = models.CharField(max_length=100)

    def __str__(self):
        return f"Traffic Closure, datetime: {self.date, self.time}, message: {self.message}"

    def create_traffic_closure(self, date, time, message, *args, **kwargs):
        self.message = message
        self.date = date
        self.time = time
        super().save(*args, **kwargs)

    def update_traffic_closure(self, date, time, message, *args, **kwargs):
        if message is not None:
            self.message = message
        if date is not None:
            self.date = date
        if time is not None:
            self.time = time
        super().save(*args, **kwargs)

    def delete_traffic_closure(self, *args, **kwargs):
        super(TrafficClosure, self).delete(*args, **kwargs)

    def get_traffic_closure(self, message):
        return TrafficClosure.objects.get(message=message)

    @classmethod
    def search_traffic_closures(cls, keyword):
        return cls.objects.filter(message__icontains=keyword)

    @classmethod
    def trafficclosureall(cls):
        return cls.objects.all()

    @classmethod
    def get_live_traffic_closures(cls):
        response = requests.get('http://datamall2.mytransport.sg/ltaodataservice/TrafficIncidents', headers=headers)

        data = response.json()["value"]
        data = json.dumps([obj for obj in data])
        df = pd.read_json(data)
        df[['Date', 'Time']] = df['Message'].str.extract(r'\((.*?)\)(.*?) ')
        df['Message'] = df['Message'].str.replace(r'\((.*?)\)(.*?) ', '', regex=True)
        current_year = datetime.datetime.now().year
        df['Date'] = df['Date'] + '/' + str(current_year)

        closures = df.loc[df['Type'] == "Road Block"]

        traffic_closures = []

        for index, row in closures.iterrows():
            date = row["Date"]
            time = row["Time"]
            message = row['Message']
            # location = row["Latitude"] + row["Longitude"]
            # or use OneMap API to reverse geocode the lat long to an address, but OneMap hasn't replied me yet

            traffic_closure = cls(date=date, time=time, message=message)
            traffic_closure.save()
            traffic_closures.append(traffic_closure)

        return traffic_closures


class TrafficAccident(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=20)
    message = models.CharField(max_length=100)

    def __str__(self):
        return f"Traffic Accident, datetime: {self.date, self.time}, message: {self.message}"

    def create_traffic_accident(self, date, time, message, *args, **kwargs):
        self.message = message
        self.date = date
        self.time = time
        super().save(*args, **kwargs)

    def update_traffic_accident(self, date, time, message, *args, **kwargs):
        if message is not None:
            self.message = message
        if date is not None:
            self.date = date
        if time is not None:
            self.time = time
        super().save(*args, **kwargs)

    def delete_traffic_accident(self, *args, **kwargs):
        super(TrafficAccident, self).delete(*args, **kwargs)

    def get_traffic_accident(self, message):
        return TrafficAccident.objects.get(message=message)

    @classmethod
    def search_traffic_accidents(cls, keyword):
        return cls.objects.filter(message__icontains=keyword)

    @classmethod
    def trafficaccidentall(cls):
        return cls.objects.all()

    @classmethod
    def get_live_traffic_accidents(cls):
        response = requests.get('http://datamall2.mytransport.sg/ltaodataservice/TrafficIncidents', headers=headers)

        data = response.json()["value"]
        data = json.dumps([obj for obj in data])
        df = pd.read_json(data)
        df[['Date', 'Time']] = df['Message'].str.extract(r'\((.*?)\)(.*?) ')
        df['Message'] = df['Message'].str.replace(r'\((.*?)\)(.*?) ', '', regex=True)
        current_year = datetime.datetime.now().year
        df['Date'] = df['Date'] + '/' + str(current_year)

        accidents = df.loc[df['Type'] == "Accident"]

        traffic_accidents = []

        for index, row in accidents.iterrows():
            date = row["Date"]
            time = row["Time"]
            message = row['Message']
            # location = row["Latitude"] + row["Longitude"]
            # or use OneMap API to reverse geocode the lat long to an address, but OneMap hasn't replied me yet

            traffic_accident = cls(date=date, time=time, message=message)
            traffic_accident.save()
            traffic_accidents.append(traffic_accident)

        return traffic_accidents
"""


