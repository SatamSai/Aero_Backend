# Generated by Django 4.0.2 on 2022-04-22 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_posts'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Posts',
        ),
    ]
