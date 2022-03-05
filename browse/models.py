from django.db import models
import random

# Create your models here.


class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    firstname = models.CharField(blank=True, null=True, max_length=20)

    def get_qte_books(self, books):
        c = 0
        for i in books:
           if i.author == self.author_id:
               c += 1
        return c

    def __str__(self):
        if self.firstname:
            chaine = self.name + " " + self.firstname
            return chaine
        return self.name


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Format(models.Model):
    format_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Language(models.Model):
    language_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=3)

    def __str__(self):
        return self.name


class Books(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    is_borrowed = models.BooleanField(default=False)
    return_date = models.DateField(blank=True, null=True)
    ref = models.CharField(max_length=6, blank=True, null=True)
    desc = models.TextField(max_length=10000, blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    format = models.ForeignKey(Format, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def create_ref(self):
        self.ref = self.title[0] + self.author.name[0] + str(random.randint(1000, 9999))

    def __str__(self):
        return self.title


class Comic(Books):
    comic_id = models.AutoField(primary_key=True)
    color = models.BooleanField()
    drawer = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Users(models.Model):
    login = models.CharField(max_length=22, blank=True, null=True)
    name = models.CharField(max_length=20)
    firstname = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    rank = models.IntegerField(default=1)
    borrow = models.ManyToManyField(Books, blank=True, null=True)

    def __str__(self):
        return self.name[0].lower() + "." + self.firstname.lower()
