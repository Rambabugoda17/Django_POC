from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


# Create your models here.


# class Employee(models.Model):
#     user_id = models.CharField(max_length=30)
#     email = models.EmailField(unique=True)
#     username = models.CharField(max_length=30, blank=True, null=True)
#     is_active = models.BooleanField(default=True)
#     profile_pic = models.ImageField(null=True)
#
#     def __str__(self):
#         return self.email


class EmployeeManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class Employee(AbstractBaseUser, PermissionsMixin):
    # user_id = models.BigIntegerField(max_length=30)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    profile_pic = models.ImageField(null=True)

    objects = EmployeeManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Technologies(models.Model):
    user = models.ForeignKey(Employee, on_delete=models.CASCADE)
    skills = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.user


class Projects(models.Model):
    user = models.ForeignKey(Employee, on_delete=models.CASCADE)
    projects = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.user
