# Generated by Django 5.0.3 on 2024-03-25 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="exam",
            name="semester",
            field=models.CharField(default="", max_length=100),
        ),
    ]