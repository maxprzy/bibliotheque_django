# Generated by Django 4.0.2 on 2022-03-05 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browse', '0006_alter_author_firstname_alter_author_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drawer',
            fields=[
                ('drawer_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('firstname', models.CharField(max_length=20)),
            ],
        ),
    ]
