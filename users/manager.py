from django.apps import apps
from django.conf import settings
from django.contrib.auth.models import BaseUserManager

from core.dataclass.user_dataclass import UserDataClass


class UserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        email = self.normalize_email(email=email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault("is_superuser", True)
        admin = self.create_user(email, password, **kwargs)
        return admin

    def change_password(self, email, password):
        UserFunctionModel = apps.get_model(settings.AUTH_USER_MODEL)

        user: UserDataClass = UserFunctionModel.objects.get(email=email)

        user.set_password(password)
        user.save()

        return user
