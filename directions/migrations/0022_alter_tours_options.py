# Generated by Django 5.0.1 on 2024-05-15 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directions', '0021_alter_tours_rating'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tours',
            options={'ordering': ['-rating', '-all_rat'], 'verbose_name': 'тур', 'verbose_name_plural': 'Туры'},
        ),
    ]