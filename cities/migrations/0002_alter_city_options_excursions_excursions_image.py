# Generated by Django 5.0.1 on 2024-03-15 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ['title']},
        ),
        migrations.AddField(
            model_name='excursions',
            name='excursions_image',
            field=models.ImageField(default='excursions/excursions.jpg', upload_to='excursions/'),
        ),
    ]