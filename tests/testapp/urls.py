from __future__ import annotations

from django.urls import path

from tests.testapp.views import index

urlpatterns = [path("", index, name="index")]
