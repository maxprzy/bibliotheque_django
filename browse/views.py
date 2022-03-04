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


def precise(request, book_id):
    q = Books.objects.get(book_id=book_id)
    template = loader.get_template('browse/precise.html')
    context = {'book':q}
    return HttpResponse(template.render(context, request))

