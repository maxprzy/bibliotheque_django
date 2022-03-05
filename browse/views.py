from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import *

# Create your views here.

def index(request):
    all_books = Books.objects.order_by('title')
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




