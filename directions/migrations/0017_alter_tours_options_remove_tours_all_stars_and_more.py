# Generated by Django 5.0.1 on 2024-04-26 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directions', '0016_alter_review_value'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tours',
            options={'verbose_name': 'тур', 'verbose_name_plural': 'Туры'},
        ),
        migrations.RemoveField(
            model_name='tours',
            name='all_stars',
        ),
        migrations.RemoveField(
            model_name='tours',
            name='percent_stars',
        ),
    ]
