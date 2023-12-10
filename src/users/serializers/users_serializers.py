from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user, created = User.objects.get_or_create(**validated_data)

        return user

    class Meta:
        model = User
        fields = ("id", "email", "first_name", "last_name", "last_login", "password")
        read_only_fields = ("id", "last_login")
