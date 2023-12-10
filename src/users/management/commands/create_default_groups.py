from django.contrib.auth.models import Group, Permission
from django.core.management import BaseCommand


class Command(BaseCommand):
    groups = (
        "admins",
        "users",
    )
    permissions_groups = {
        "admins": [
            "add_session",
            "view_group",
            "add_group",
            "add_user",
            "view_session",
            "delete_contenttype",
            "change_user",
            "view_permission",
            "change_session",
            "delete_session",
            "change_group",
            "add_permission",
            "delete_group",
            "change_contenttype",
            "view_user",
            "view_contenttype",
            "add_contenttype",
            "delete_user",
            "change_permission",
            "delete_permission",
        ],
        "users": [
            "add_session",
            "view_session",
            "add_contenttype",
            "view_contenttype",
            "change_contenttype",
            "delete_contenttype",
            "view_user",
            "view_permission",
        ],
    }

    def handle(self, *args, **options):
        groups = Group.objects.filter(name__in=self.groups)
        permissions = Permission.objects.all()
        # Если групп вообще нет, то создаём
        if not groups.exists():
            for i, group in enumerate(self.groups):
                group_created = Group(id=i, name=group)
                group_permission = permissions.filter(codename__in=self.permissions_groups[group])
                group_created.save()
                group_created.permissions.set(group_permission)
        # Если только 1 группа есть, то создаем вторую
        elif groups.count() < len(self.groups):
            for i, group in enumerate(self.groups):
                group_, created = Group.objects.get_or_create(name=group)
                group_permission = permissions.filter(codename__in=self.permissions_groups[group])
                if created:
                    group_.permissions.set(group_permission)
        # Если все есть, то проверяем права и переназначаем, при необходимости
        else:
            for i, group in enumerate(self.groups):
                group_ = Group.objects.get(name=group)
                group_permission = permissions.filter(codename__in=self.permissions_groups[group])
                group_.permissions.clear()
                group_.permissions.set(group_permission)
