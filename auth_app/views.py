from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import PasswordResetView
import logging
from .models import UserPerfil

logger = logging.getLogger(__name__)


# função de teste


@login_required
def dashboard(request):
    return render(request, "pages/dashboard.html")


@login_required
def minha_conta(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        sobrenome = request.POST.get("sobrenome")
        telefone = request.POST.get("telefone")
        if request.user.is_authenticated:
            user_perfil = UserPerfil.objects.get(user=request.user)
            user_perfil.nome = nome
            user_perfil.sobrenome = sobrenome
            user_perfil.telefone = telefone
            user_perfil.save()

    return render(request, "auth_app\minha_conta\conta.html")


def atualizar_dados(request):
    ...


# função de Login
def user_login(request):
    if request.method == "POST":
        signin_email = request.POST["signin-email"]
        signin_password = request.POST["signin-password"]

        try:
            user_name = User.objects.get(email=signin_email)
            user_authenticate = authenticate(
                request, username=user_name, password=signin_password
            )
            if user_authenticate is not None:
                login(request, user=user_authenticate)
                logger.info(f"O Usuario: {user_authenticate} acabou de fazer login")
                return redirect("dashboard")
            else:
                messages.add_message(
                    request, messages.INFO, message="E-mail ou senha incorretos"
                )

        except User.DoesNotExist:
            messages.add_message(
                request,
                messages.INFO,
                message="Este e-mail, não existe",
            )
            logger.info(f"O Usuario: {User} acabou de fazer login")

    return render(request, "auth_app/user_login.html")


# função de Cadastrar
def user_signup(request):
    if request.method == "POST":
        signup_name = request.POST["signup-name"]
        signup_email = request.POST["signup-email"]
        signup_password = request.POST["signup-password"]

        # Verifica se o usuário já existe pelo nome de usuário ou endereço de e-mail
        existing_users = User.objects.filter(
            username=signup_name
        ) | User.objects.filter(email=signup_email)

        if existing_users.exists():
            # Usuário já existe, forneça uma mensagem informativa
            messages.add_message(
                request,
                messages.INFO,
                f"O usuário '{signup_name}' ou e-mail '{signup_email}' já existe no nosso sistema.",
            )
        else:
            # Usuário não existe, crie um novo usuário
            new_user = User.objects.create_user(
                signup_name.lower(), signup_email.lower(), signup_password
            )
            new_user.save()

            # Envie um e-mail de confirmação ou outras ações necessárias
            disparar_email(date=new_user)

            # Redirecione para a página de login após o cadastro bem-sucedido
            return redirect("user_login")

    return render(request, "auth_app/user_signup.html")


# função deslogar
def user_logout(request):
    return redirect("user_login")


# função de disparo de email
def disparar_email(date):
    print(f"chamei a função com os dados {date.email}")


# função de checar user
def check_user(request):
    if request.method == "POST":
        email = request.POST.get("email")

        try:
            user = User.objects.get(email=email)

            # Chame diretamente a view de redefinição de senha com os parâmetros necessários
            reset_view = PasswordResetView.as_view(
                template_name="auth_app/password_reset.html",
                success_url=reverse("password_reset_done"),  # URL de sucesso
                form_class=PasswordResetForm,  # Classe de formulário de redefinição de senha
                extra_email_context={
                    "email": email
                },  # Parâmetro extra: o email do usuário
            )

            return reset_view(request)

        except User.DoesNotExist:
            messages.add_message(
                request,
                messages.INFO,
                f"O email {email} não existe no nosso sistema",
            )

    form = PasswordResetForm()
    return render(request, "auth_app/password_reset.html", {"form": form})


from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserPerfil


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserPerfil.objects.create(user=instance)
