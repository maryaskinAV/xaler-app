from django.urls import path

from users.views import ListCreateUsersView, RetrieveUpdateUsersView

app_name = "users"
urlpatterns = [
    path("users", ListCreateUsersView.as_view(), name="list_create_users"),
    path("users/<int:id>", RetrieveUpdateUsersView.as_view(), name="list_create_users"),
]
