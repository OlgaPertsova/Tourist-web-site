# Generated by Django 5.0.1 on 2024-05-15 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0006_alter_excursions_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='excursions',
            options={'ordering': ['-duration', 'price'], 'verbose_name': 'экскурсию', 'verbose_name_plural': 'Экскурсии'},
        ),
    ]
