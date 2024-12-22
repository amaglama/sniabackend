from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter
from oauth2_provider import views


app_name = "external"

router = DefaultRouter()

base_urlpatterns = [
    #re_path(r"^token/$", views.TokenView.as_view(), name="token"),
    #re_path(r"^revoke_token/$", views.RevokeTokenView.as_view(), name="revoke-token"),
]





urlpatterns = base_urlpatterns
