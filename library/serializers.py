import datetime

from rest_framework import serializers
from library.models import Author, Book, BookIssue


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


def validate(value):
    """
    Валидатор даты возврата книги.
    Если дата возврата совпадает с датой выдачи, бросает ошибку.
    :param value:
    :return:
    """
    if value == datetime.date.today():
        raise serializers.ValidationError("Нельзя вернуть книгу в день выдачи")
    return value


class BookIssueSerializer(serializers.ModelSerializer):
    borrow_date = serializers.DateField(validators=[validate])

    class Meta:
        model = BookIssue
        fields = '__all__'
        read_only_fields = ['borrow_date', 'is_overdue']
