from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from djongo import models
import uuid

class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    role = models.CharField(max_length=30, default='User Admin')  # Single role for User Admin

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
