# Generated by Django 5.2.3 on 2025-06-25 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="proyecto",
            old_name="usuario",
            new_name="usuarios",
        ),
    ]
