# Generated by Django 4.1.6 on 2023-10-05 06:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('women', '0002_remove_category_slug_remove_women_photo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='women',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]
