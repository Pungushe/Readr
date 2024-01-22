from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = "author"
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"