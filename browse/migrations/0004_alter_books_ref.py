# Generated by Django 3.2.8 on 2022-03-02 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browse', '0003_alter_users_borrow'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='ref',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]