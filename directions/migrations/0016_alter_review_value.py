# Generated by Django 5.0.1 on 2024-04-25 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directions', '0015_alter_review_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='value',
            field=models.IntegerField(default=0, verbose_name='Сколько звезд'),
        ),
    ]
