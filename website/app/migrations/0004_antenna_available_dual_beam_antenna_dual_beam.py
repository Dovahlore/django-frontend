# Generated by Django 5.0.3 on 2024-07-05 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0003_alter_admin_id_alter_antenna_id_alter_log_id_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="antenna",
            name="available_dual_beam",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="antenna",
            name="dual_beam",
            field=models.IntegerField(default=0),
        ),
    ]
