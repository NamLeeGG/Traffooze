from django.db import models

# Create your models here.
"""
# Custom user
class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    ROLE =  (('UserAdmin', 'UserAdmin'),
             ('CinemaOwner', 'CinemaOwner'),
             ('CinemaManager', 'CinemaManager'),
             ('Customer', 'Customer'))
    role = models.CharField(max_length=30, choices=ROLE, default='Customer')

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    
    def usercreate(self, username, password, email, role, *args, **kwargs):
        self.username = username
        self.email = email
        self.role = role
        if password is not None:
            self.password = make_password(password)
        super().save(*args, **kwargs)
    
    def userupdate(self, email, password, *args, **kwargs):
        if email is not None:
            self.email = email
        if password is not None:
            self.password = make_password(password)
        super().save(*args, **kwargs)
    
    def userdelete(self, *args, **kwargs):
        super(User, self).delete(*args, **kwargs)

    def userauthenticate(self, request, username, password):
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)   
        else:
            token = None
        return token

    def userget(self, username):
        return User.objects.get(username = username)
    
    @classmethod
    def usersearch(cls, keyword):
        return cls.objects.filter(username__icontains=keyword)
    
    @classmethod
    def userall(cls):
        return cls.objects.all()
    
    def userlogout(self, request):
        logout(request)
"""