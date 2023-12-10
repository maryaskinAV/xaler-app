import logging

from django.core.management import BaseCommand

from users.models import User

logger = logging.getLogger(__file__)


class Command(BaseCommand):
    """
    Команда создание суперпользователя.
    """

    def handle(self, *args, **options):
        superuser, created = User.objects.get_or_create(
            email="super@user.adm",
            first_name="Super",
            last_name="Admin",
            is_active=True,
            is_superuser=True,
            is_staff=True,
        )

        if created:
            superuser.set_password("qwe123QE")
        superuser.save(update_fields=["password"])
