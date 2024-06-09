from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):        
        if not email:
            raise ValueError('O usuário deve ter um endereço de email!')  # Exibe um erro para user sem email
        
        email = self.normalize_email(email)  # Converte o email em uma forma canônica.
        user = self.model(email=email, **extra_fields)  # Cria uma instância do modelo de user
        user.set_password(password)  # Define senha do user, gerando um hash seguro da senha
        user.save(using=self._db) # Salva a instância no banco de dados

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Administrador deve ter is_staff=True')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Administrador deve ter is_superuser=True')
        
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=80, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
    