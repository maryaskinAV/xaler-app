from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    # project urls
    path("auth/", include("users.urls.auth_urls")),
    path("users/", include("users.urls.users_urls")),
    # Swagger schema urls
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
]
