# Generated by Django 4.0.2 on 2022-03-06 01:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('browse', '0009_books_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='borrow',
        ),
        migrations.DeleteModel(
            name='Comic',
        ),
        migrations.DeleteModel(
            name='Drawer',
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]