from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .models import *

# Create your views here.

def index(request):
    all_books = Book.objects.order_by('title')
    template = loader.get_template('browse/index.html')
    context = {'all_books':all_books}
    return HttpResponse(template.render(context,request))

def book(request, book_id):
    q = Books.objects.get(book_id=book_id)
    template = loader.get_template('browse/precise.html')
    context = {'book':q}
    return HttpResponse(template.render(context, request))


def authors(request):
    q = Author.objects.order_by('name')
    template = loader.get_template('browse/authors.html')
    context = {'all_authors': q}
    return HttpResponse(template.render(context, request))

def author(request, author_id):
    q = Books.objects.filter(author=author_id)
    template = loader.get_template('browse/author.html')
    context = {'books_by_author': q}
    return HttpResponse(template.render(context, request))

def categories(request):
    q = Category.objects.order_by('name')
    template = loader.get_template('browse/categories.html')
    context = {'all_categories': q}
    return HttpResponse(template.render(context, request))

def category(request, category_id):
    q = Books.objects.filter(category=category_id)
    template = loader.get_template('browse/category.html')
    context = {'books_by_category': q}
    return HttpResponse(template.render(context, request))

def formats(request):
    q = Format.objects.order_by('name')
    template = loader.get_template('browse/formats.html')
    context = {'all_formats': q}
    return HttpResponse(template.render(context, request))

def format(request, format_id):
    q = Books.objects.filter(format=format_id)
    template = loader.get_template('browse/format.html')
    context = {'books_by_format': q}
    return HttpResponse(template.render(context, request))

def borrow(request, book_id):
    book = get_object_or_404(Books, book_id=book_id)
    book.is_borrowed = True
    book.return_date = datetime.date.today() + datetime.timedelta(days=15)
    book.borrowuser.add(request.user)
    book.save()
    template = loader.get_template('browse/borrowed.html')
    context = {'book':book}
    return HttpResponse(template.render(context, request))

def register(request):
    return render(request, 'browse/register.html')

def registered(request):
    name = request.POST['user_name']
    firstname = request.POST['user_firstname']
    pwd = request.POST['user_pwd']
    email = request.POST['user_email']
    username = firstname[0].lower() + "." + name.lower()
    user = User.objects.create_user(username, email, pwd)
    user.last_name = name
    user.first_name = firstname
    user.save()
    template = loader.get_template('browse/registered.html')
    context = {'username': username, 'email': email, 'firstname': firstname}
    return HttpResponse(template.render(context, request))


def my_login(request):
    return render(request, 'browse/login.html')


def logged(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    template = loader.get_template('browse/logged.html')
    invalid_template = loader.get_template('browse/error_log.html')
    context = {'user': user}
    if user is not None:
        login(request, user)
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponse(invalid_template.render(context, request))

def my_logout(request):
    logout(request)
    return render(request, 'browse/logout.html')

def profile(request):
    borrows = Books.objects.filter(borrowuser=request.user)
    template = loader.get_template('browse/profile.html')
    context = {'borrows': borrows, 'qte': len(borrows)}
    return HttpResponse(template.render(context, request))


def goback(request, book_id):
    book = get_object_or_404(Books, book_id=book_id)
    book.is_borrowed = False
    book.return_date = None
    book.borrowuser.remove(request.user)
    book.save()
    return render(request, 'browse/goback.html')

