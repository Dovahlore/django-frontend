# Generated by Django 5.0.3 on 2024-07-11 01:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0006_remove_antenna_create_time"),
    ]

    operations = [
        migrations.RenameField(
            model_name="meta_task_list",
            old_name="task_id",
            new_name="belong_to_task",
        ),
    ]
