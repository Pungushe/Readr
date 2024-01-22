from django.db import models

from author.models import Author

class Book(models.Model):
    WANTED='нужно прочитать'
    READING= 'сейчас читаю'
    UNREAD='не прочитанные'
    ALREADY_READ='уже прочитанные'
    
    STATUS_CHOICES = (
        (UNREAD, 'Не прочитанные'),
        (READING, 'Сейчас читаю'),
        (ALREADY_READ, 'Уже прочитанные'),
        (WANTED, 'Нужно прочитать'),
    )
    
    title = models.CharField(max_length=255, verbose_name="Название")
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE, verbose_name="Автор")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="UNREAD", verbose_name="Статус")
    
    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        db_table = "book"
        ordering = ("title",)
        verbose_name = "Книга"
        verbose_name_plural = "Книги"