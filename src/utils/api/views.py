from rest_framework.generics import GenericAPIView
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response


class RetrieveUpdateAPIView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin):
    def get(self, request, *args, **kwargs) -> Response:
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs) -> Response:
        return self.update(request, *args, **kwargs)
