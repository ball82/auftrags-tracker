from django.urls import path
from . import views

urlpatterns = [
    path("", views.auftrag_liste, name="auftrag-liste")
]