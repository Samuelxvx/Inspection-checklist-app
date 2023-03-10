# Generated by Django 4.1.5 on 2023-02-08 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Inspection",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("count", models.IntegerField(blank=True, null=True)),
                (
                    "location",
                    models.CharField(
                        choices=[
                            ("管理棟ＣＰＵ室", "管理棟ＣＰＵ室"),
                            ("工場棟2F 外注ｴﾘｱ", "工場棟2F 外注ｴﾘｱ"),
                            ("倉庫７", "倉庫７"),
                            ("管理棟2F EPS1", "管理棟2F EPS1"),
                            ("鍵返却", "鍵返却"),
                        ],
                        max_length=50,
                        null=True,
                    ),
                ),
                ("checkTarget", models.CharField(blank=True, max_length=50)),
                ("checkDetail", models.CharField(blank=True, max_length=50)),
                (
                    "manufacturerModel",
                    models.CharField(blank=True, default="", max_length=100, null=True),
                ),
                ("method", models.CharField(default="", max_length=50)),
                ("normalState", models.CharField(blank=True, max_length=255)),
                (
                    "username",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("疋田", "疋田"),
                            ("若狭", "若狭"),
                            ("⻄田（紀）", "⻄田（紀）"),
                            ("伊藤", "伊藤"),
                            ("上本", "上本"),
                            ("遠藤", "遠藤"),
                            ("⻄田（⼤）", "⻄田（⼤）"),
                        ],
                        max_length=60,
                        null=True,
                    ),
                ),
                ("date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
