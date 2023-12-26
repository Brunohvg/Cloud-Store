from django.urls import path
from . import views

app_name = "calculadora_app"

urlpatterns = [
    path("", views.calculadora_app, name="calculadora_frete"),  # Rota calculadora frete
]
