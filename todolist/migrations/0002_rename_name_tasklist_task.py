# Generated by Django 5.0.3 on 2024-05-07 09:52

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("todolist", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="tasklist",
            old_name="name",
            new_name="task",
        ),
    ]
