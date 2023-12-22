from django.urls import path
from . import views

from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", views.user_login, name="user_login"),  # Rota Logar User
    path("signup/", views.user_signup, name="user_signup"),  # Rota Cadastrar User
    path("logout/", views.user_logout, name="user_logout"),  # Deslogar User
    path("password/", views.check_user, name="check_user"),
    path(
        "reset_password_sent/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="auth_app/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "password_reset_confirm/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset_password_complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="auth_app/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("account/", views.minha_conta, name="minha_conta"),
]
