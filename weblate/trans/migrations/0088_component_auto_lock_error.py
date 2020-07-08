# Generated by Django 3.0.7 on 2020-06-22 14:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("trans", "0087_auto_20200615_0747"),
    ]

    operations = [
        migrations.AddField(
            model_name="component",
            name="auto_lock_error",
            field=models.BooleanField(
                default=settings.DEFAULT_AUTO_LOCK_ERROR,
                help_text="Whether the component should be locked on repository errors.",
                verbose_name="Lock on error",
            ),
        ),
    ]