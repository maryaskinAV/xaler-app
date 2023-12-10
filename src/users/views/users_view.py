from rest_framework.generics import ListCreateAPIView, DestroyAPIView

from users.models import User
from users.serializers import UserSerializer
from utils.api.views import RetrieveUpdateAPIView


class ListCreateUsersView(ListCreateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(is_active=True)


class RetrieveUpdateUsersView(RetrieveUpdateAPIView):
    pass


class DeleteUserView(DestroyAPIView):
    pass
