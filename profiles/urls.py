from django.urls import path
from . import views
urlpatterns = [
    path("", views.CreateProfView.as_view())
]
