# Generated by Django 5.0.1 on 2024-04-25 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directions', '0014_alter_review_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='value',
            field=models.CharField(choices=[('ONE', '★'), ('TWO', '★★'), ('THREE', '★★★'), ('FOUR', '★★★★'), ('FIFE', '★★★★★')], max_length=50, verbose_name='Сколько звезд'),
        ),
    ]
