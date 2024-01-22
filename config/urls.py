from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    # главная страница
    path('', include('core.urls', namespace='core')),
    # страница авторов
    path('author/', include('author.urls', namespace='author')),
    # страница книг
    path('books/', include('books.urls', namespace='books')),
]
