from django.urls import include, path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'browse'
urlpatterns = [
    path('', views.index, name='index'),
    path('authors/', views.authors, name="authors"),
    path('authors/<int:author_id>/', views.author, name="author"),
    path('categories/', views.categories, name="categories"),
    path('categories/<int:category_id>/', views.category, name="category"),
    path('formats/', views.formats, name="formats"),
    path('formats/<int:format_id>/', views.format, name="format"),
    path('books/<int:book_id>/', views.book, name="book"),
    path('books/<int:book_id>/borrow/', views.borrow, name="borrow"),
    path('accounts/register/', views.register, name="register"),
    path('accounts/registered/', views.registered, name='registered'),
    path('accounts/login/', views.my_login, name='login'),
    path('accounts/logged/', views.logged, name='logged'),
    path('accounts/logout/', views.my_logout, name='logout'),
    path('accounts/profile/', views.profile, name='profile'),
    path('accounts/goback/<int:book_id>/', views.goback, name='goback'),
]
