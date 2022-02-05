from django.urls import path

from . import views

urlpatterns = [
path("<str:id>", views.personDetail, name="detail"),
path("", views.personCreate, name="create"),
]