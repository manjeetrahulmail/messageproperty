from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, whatsapp, first_name, last_name, password=None):
        if not email:
            return ValueError('User must have an email address')
        if not first_name:
            return ValueError('User must have a first name')
        if not last_name:
            return ValueError('User must have a last name')
        if not whatsapp:
            return ValueError('User must have a whatsapp number')

        user = self.model(
            email=self.normalize_email(email),
            whatsapp=whatsapp,
            first_name=first_name,
            last_name=last_name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, whatsapp, first_name, last_name, password):
        user = self.create_user(
            email=self.normalize_email(email),
            whatsapp=whatsapp,
            password=password,
            first_name=first_name,
            last_name=last_name
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user


# Create your models here.
class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name='Email Address', max_length=60, unique=True)
    username = None
    whatsapp = models.CharField(verbose_name='Whatsapp Number', max_length=10, unique=True)

    clicks = models.IntegerField(verbose_name='Profile Visits', default=0)

    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    first_name = models.CharField(verbose_name='First Name', max_length=25)
    last_name = models.CharField(verbose_name='Last Name', max_length=25)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'whatsapp']

    objects = CustomUserManager()

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' - ' + self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True