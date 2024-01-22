from django.urls import path

from . import views

app_name = 'book'

urlpatterns = [
    path('', views.main_book, name='main'),
    path('add-book/', views.add_book, name='add'),
    path('<int:pk>/', views.detail_book, name='detail'),
    path('<int:pk>/edit/', views.edit_book, name='edit'),
    path('<int:pk>/delete/', views.delete_book, name='delete'),
]
