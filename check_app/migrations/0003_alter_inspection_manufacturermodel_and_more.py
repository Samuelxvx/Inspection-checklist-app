# Generated by Django 4.1.5 on 2023-02-09 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("check_app", "0002_inspection_itemslist"),
    ]

    operations = [
        migrations.AlterField(
            model_name="inspection",
            name="manufacturerModel",
            field=models.TextField(blank=True, default="", max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="inspection",
            name="normalState",
            field=models.TextField(blank=True, max_length=255),
        ),
    ]
