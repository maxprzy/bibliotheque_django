from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(Books)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Language)
admin.site.register(Format)
admin.site.register(Comic)
admin.site.register(Users)
