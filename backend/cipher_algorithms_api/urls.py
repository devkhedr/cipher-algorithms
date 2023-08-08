from django.urls import path
from .views import *
urlpatterns = [
    path("encrypt/", EncryptView.as_view(), name="encrypt"),
    path("decrypt/", DecryptView.as_view(), name="decrypt"),
]
