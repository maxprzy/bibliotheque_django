from django.db import models
import random

# Create your models here.


class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    firstname = models.CharField(blank=True, null=True, max_length=20)

    def __str__(self):
        if self.firstname:
            chaine = self.name + " " + self.firstname
            return chaine
        return self.name


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)

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
    ref = models.CharField(max_length=6)
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
