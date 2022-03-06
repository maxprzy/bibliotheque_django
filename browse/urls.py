from django.urls import path
from . import views

app_name = 'browse'
urlpatterns = [
    path('', views.index, name='index'),
    path('authors/', views.authors, name="authors"),
    path('categories/', views.categories, name="categories"),
    path('formats/', views.formats, name="formats"),
    path('book/<int:book_id>/', views.book, name="book"),
    path('author/<int:author_id>/', views.author, name="author"),
    path('category/<int:category_id>/', views.category, name="category"),
    path('format/<int:format_id>/', views.format, name="format"),
    path('book/<int:book_id>/borrow/', views.borrow, name="borrow"),
]
