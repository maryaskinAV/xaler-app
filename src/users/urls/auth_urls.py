from django.urls import path

from users.views import LoginView, RegistrationView, ForgetPasswordView

app_name = "auth"

urlpatterns = [
    path("login", LoginView.as_view(), name="login_view"),
    path("registration", RegistrationView.as_view(), name="registration_view"),
    path("forget_password", ForgetPasswordView.as_view(), name="forget-password_view"),
]
