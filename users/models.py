from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None

    first_name = models.CharField(
        max_length=50,
        verbose_name="Имя",
        help_text="Введите ваше имя",
    )

    last_name = models.CharField(
        max_length=50,
        verbose_name="Фамилия",
        help_text="Введите вашу фамилию",
    )

    email = models.EmailField(unique=True, verbose_name="Email")

    avatar = models.ImageField(
        upload_to="users/avatars/",
        verbose_name="Аватар",
        **NULLABLE,
        help_text="Загрузите фото",
    )

    phone_number = PhoneNumberField(
        **NULLABLE, verbose_name="Номер телефона", help_text="Введите номер телефона"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
