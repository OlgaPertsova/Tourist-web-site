# Generated by Django 5.0.1 on 2024-04-14 13:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_profile_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='verify',
            field=models.BooleanField(default=False, verbose_name='Подтверждение почты'),
        ),
        migrations.CreateModel(
            name='Verification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.UUIDField(unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('expiration', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
            options={
                'verbose_name': 'верификацию',
                'verbose_name_plural': 'Верификация по почте',
            },
        ),
    ]