# Generated by Django 5.0.1 on 2024-04-30 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directions', '0020_alter_tours_all_rat_alter_tours_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tours',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=3, verbose_name='Рейтинг'),
        ),
    ]