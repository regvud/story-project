from django.urls import path

from users.views import (
    UserListView,
    UserRetrieveUpdateDestroyView,
    UserCreateView,
    ChangeEmailUpdateView,
    ChangePasswordUpdateView,
    
    ProfileListView,
    ProfileRetrieveUpdateView,
    
    AccountListView,
    AccountRetrieveUpdateView,
)


urlpatterns = [
    path("user-list", UserListView.as_view(), name="user_list"),
    path("create", UserCreateView.as_view(), name="user_create"),
    path("<int:pk>", UserRetrieveUpdateDestroyView.as_view(), name="user_list"),
    path("<int:pk>/email", ChangeEmailUpdateView.as_view(), name="user_email_update"),
    path("<int:pk>/pass", ChangePasswordUpdateView.as_view(), name="user_pass_update"),
    
    # profile
    path("profile-list", ProfileListView.as_view(), name="profile_list"),
    path("<int:pk>/profile", ProfileRetrieveUpdateView.as_view(), name="profile_retrieve_update"),
    
    # account
    path("account-list", AccountListView.as_view(), name="account_list"),
    path("<int:pk>/account", AccountRetrieveUpdateView.as_view(), name="account_retrieve_update"),
]
