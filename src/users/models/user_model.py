from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone

from django.utils.translation import gettext_lazy as _

from utils.uploaders import upload_image


class UserManager(BaseUserManager):
    """
    Менеджер для перекрытой модели пользователя
    """

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if password is not None:
            try:
                validate_password(password)
            except ValidationError as e:
                raise ValueError({"password": _("Password can't be set. Update password and try again.")})
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email=email, password=password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_admin", True)
        return self._create_user(email=email, password=password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    Переопределенная модель пользователя
    """

    email = models.EmailField(_("email address"), unique=True)
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    mid_name = models.CharField(_("middle name"), max_length=150, blank=True, null=True)

    avatar = models.ImageField(_("user image"), upload_to=upload_image, blank=True, null=True)

    is_active = models.BooleanField(_("active"), default=False)
    is_staff = models.BooleanField(_("staff status"), default=False)
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    class Meta:
        ordering = ["email", "id"]
        verbose_name = _("user")
        verbose_name_plural = _("users")

    @property
    def get_avatar(self):
        if self.avatar:
            return self.avatar.url
        return "/static/images/default-avatar.png"
