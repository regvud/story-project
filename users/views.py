from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.authentication import get_user_model
from rest_framework.generics import (
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
    UpdateAPIView,
)
from rest_framework import status

from users.serializers import (
    ProfileSerializer,
    UserSerializer,
    AccountSerializer,
    ChangeEmailSerializer,
    ChangePasswordSerializer,
)
from users.models import (
    ProfileModel,
    AccountModel,
)


UserFunctionModel = get_user_model()



class UserListView(ListAPIView):
    queryset = UserFunctionModel.objects.all()
    serializer_class = UserSerializer


class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = UserFunctionModel
    serializer_class = UserSerializer


class UserCreateView(CreateAPIView):
    queryset = UserFunctionModel
    serializer_class = UserSerializer


class ChangeEmailUpdateView(UpdateAPIView):
    def patch(self, request: Request, *args, **kwargs):
        new_email = request.data.get("email", None)
        if new_email is None:
            return Response({"error": "Email is required"}, status.HTTP_400_BAD_REQUEST)
        
        user_pk = kwargs.get("pk")
        try:
            user = UserFunctionModel.objects.get(pk=user_pk)
        except UserFunctionModel.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
        user.email = new_email
        user.save()
        
        serializer = ChangeEmailSerializer(user)
        
        return Response(serializer.data, status.HTTP_200_OK)
        

# ###################################################################


class ProfileListView(ListAPIView):
    queryset = ProfileModel.objects.all()
    serializer_class = ProfileSerializer


class ProfileRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = ProfileModel
    serializer_class = ProfileSerializer


class ChangePasswordUpdateView(UpdateAPIView):
        serializer_class = ChangePasswordSerializer

        def update(self, request, *args, **kwargs):
            
            user_pk = kwargs.get("pk")
            try:
                user = UserFunctionModel.objects.get(pk=user_pk)
            except UserFunctionModel.DoesNotExist:
                return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = self.get_serializer(data=request.data)

            if serializer.is_valid():
                # Check old password
                if not user.check_password(serializer.data.get("old_password")):
                    return Response(
                        {"old_password": "Wrong password."},
                        status.HTTP_400_BAD_REQUEST
                    )
                    
                user.set_password(serializer.data.get("new_password"))
                user.save()
                
                return Response(
                    {'message': 'Password updated successfully'},
                    status.HTTP_200_OK,
                )

            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


# ###################################################################


class AccountListView(ListAPIView):
    queryset = AccountModel.objects.all()
    serializer_class = AccountSerializer


class AccountRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = AccountModel
    serializer_class = AccountSerializer
