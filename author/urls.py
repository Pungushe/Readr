from django.urls import path

from . import views

app_name = 'author'

urlpatterns = [
    path('', views.index, name='index'),
    # Добавить автора
    path('add-author/', views.add_author, name='add'),
    # Детали
    path('<int:pk>/', views.detail, name='detail'),
]
