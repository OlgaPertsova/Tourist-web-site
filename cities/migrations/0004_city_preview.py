# Generated by Django 5.0.1 on 2024-03-19 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0003_alter_excursions_excursions_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='preview',
            field=models.TextField(blank=True, null=True),
        ),
    ]