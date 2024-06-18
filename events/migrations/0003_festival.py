# Generated by Django 5.0.1 on 2024-03-20 11:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0004_city_preview'),
        ('events', '0002_lifehacks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Festival',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('info', models.TextField(blank=True)),
                ('date_of_the', models.DateField()),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cities.city')),
            ],
        ),
    ]