# Generated by Django 5.0.1 on 2024-02-28 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_place_place_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Place',
        ),
    ]
