from django.contrib.auth import get_user_model
from django.db.transaction import atomic
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from users.models import AccountModel, ProfileModel

UserFunctionModel = get_user_model()


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = (
            "id",
            "name",
            "surname",
            "status",
            "age",
            "bio",
            "image",
        )

        read_only_fields = ("id",)


class ProfileImageSerializer(ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ("image",)
        extra_kwargs = {"image": {"required": True}}


class AccountSerializer(ModelSerializer):
    class Meta:
        model = AccountModel
        fields = (
            "id",
            "is_writer",
            "is_premium",
            "expire_premium",
        )


class UserSerializer(ModelSerializer):
    profile = ProfileSerializer()
    account = AccountSerializer()

    class Meta:
        model = UserFunctionModel
        fields = (
            "id",
            "email",
            "username",
            "password",
            "is_active",
            "is_block",
            "profile",
            "account",
            "create_at",
            "update_at",
        )
        read_only_fields = (
            "id",
            "create_at",
            "update_at",
        )
        extra_kwargs = {"password": {"write_only": True}}

    @atomic
    def create(self, validated_data):
        profile = validated_data.pop("profile")
        account = validated_data.pop("account")
        profile = ProfileModel.objects.create(**profile)
        account = AccountModel.objects.create(**account)
        user = UserFunctionModel.objects.create_user(
            **validated_data, profile=profile, account=account
        )
        return user

    # def update(self, instance, validated_data):
    #     profile_data = validated_data.pop("profile")

    #     profile_serializer = self.fields["profile"]
    #     profile_instance = instance.profile

    #     profile_serializer.update(profile_instance, profile_data)

    #     instance.save()
    #     return instance


class UserPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFunctionModel
        fields = ("password", )
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        new_password = UserFunctionModel.objects.change_password(**validated_data)
        return new_password


class ChangePasswordSerializer(serializers.Serializer):
    model = UserFunctionModel
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class ChangeEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFunctionModel
        fields = ("email", )
