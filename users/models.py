from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from users.manager import UserManager
from core.models import CoreModel


class ProfileModel(CoreModel):
    class Meta:
        db_table = "profile_users"

    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    status = models.CharField(max_length=100)
    age = models.IntegerField()
    bio = models.CharField(max_length=255)
    image = models.ImageField(upload_to="image/", blank=True, null=True)


class AccountModel(CoreModel):
    class Meta:
        db_table = "account_users"

    is_writer = models.BooleanField(default=False)
    is_premium = models.BooleanField(default=False)
    expire_premium = models.DateTimeField(null=True)


class UserModel(AbstractBaseUser, PermissionsMixin, CoreModel):
    class Meta:
        db_table = "auth_users"

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    username = models.CharField(max_length=20)
    # base status
    is_active = models.BooleanField(default=False)
    is_block = models.BooleanField(default=False)
    # profile
    profile = models.OneToOneField(
        ProfileModel, on_delete=models.SET_NULL, related_name="user", null=True
    )
    # type_account
    account = models.OneToOneField(
        AccountModel, on_delete=models.CASCADE, related_name="user", null=True
    )
    USERNAME_FIELD = "email"

    objects = UserManager()
    # settings
