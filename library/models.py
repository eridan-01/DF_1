from django.db import models
from django.utils import timezone
import datetime

from users.models import NULLABLE, User


class Author(models.Model):
    first_name = models.CharField(
        max_length=100,
        verbose_name="Имя",
        help_text="Введите имя автора"
    )

    last_name = models.CharField(
        max_length=100,
        verbose_name="Фамилия",
        help_text="Введите фамилию автора"
    )

    date_of_birth = models.DateField(
        **NULLABLE,
        verbose_name="Дата рождения",
        help_text="Введите дату рождения автора"
    )

    biography = models.TextField(
        **NULLABLE,
        verbose_name="Биография",
        help_text="Введите биографию автора"
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class Book(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Название",
        help_text="Введите название книги"
    )

    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="books",
        verbose_name="Автор",
        help_text="Выберите автора"
    )

    genre = models.CharField(
        max_length=100,
        verbose_name="Жанр",
        help_text="Введите жанр"
    )

    published_date = models.DateField(
        verbose_name="Дата публикации",
        help_text="Введите дату публикации"
    )

    isbn = models.CharField(
        max_length=13,
        unique=True,
        verbose_name="ISBN",
        help_text="Введите ISBN"
    )

    available_copies = models.PositiveIntegerField(
        default=1,
        verbose_name="Количество доступных копий"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"


class BookIssue(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name="issues",
        verbose_name="Книга"
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="borrowed_books",
        verbose_name="Пользователь"
    )

    borrow_date = models.DateField(
        default=datetime.date.today,
        verbose_name="Дата выдачи",
        help_text="Введите дату выдачи"
    )

    due_date = models.DateField(
        verbose_name="Срок возврата",
        help_text="Введите срок возврата"
    )

    return_date = models.DateField(
        **NULLABLE,
        verbose_name="Дата возврата",
        help_text="Введите дату возврата"
    )

    status = models.CharField(
        max_length=20,
        choices=[('borrowed', 'Выдана'), ('returned', 'Возвращена')],
        default='borrowed',
        verbose_name="Статус"
    )

    def __str__(self):
        return f"{self.book.title} - {self.user.first_name} {self.user.last_name}"

    class Meta:
        verbose_name = "Выдача книги"
        verbose_name_plural = "Выдачи книг"

    def is_overdue(self):
        return self.return_date is None and self.due_date < timezone.now().date()
