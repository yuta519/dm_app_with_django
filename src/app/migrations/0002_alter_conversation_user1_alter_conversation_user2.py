# Generated by Django 4.1.13 on 2024-01-09 22:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="conversation",
            name="user1",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user1",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="conversation",
            name="user2",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user2",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
