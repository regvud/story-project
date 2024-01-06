from django.urls import include, path

urlpatterns = [
    path("", include("core.swagger")),
    path("user/", include("users.urls"), name="users"),
]
