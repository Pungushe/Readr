from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    email = models.EmailField()
    bio = models.TextField(verbose_name="Биография")
    birthdate = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    
    class Meta:
        db_table = "author"
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"