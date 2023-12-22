from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserPerfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100, blank=True)
    telefone = models.CharField(max_length=15, blank=True)
    """
    def pre_save(self, *args, **kwargs):
        if not self.nome:
            raise ValueError("O nome é obrigatório")
        if not self.telefone:
            raise ValueError("O telefone é obrigatório")
    """

    def __str__(self) -> str:
        return self.nome
