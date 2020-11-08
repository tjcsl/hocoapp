# Generated by Django 3.0.8 on 2020-07-16 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("scores", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="scoreboard",
            name="freshman_score",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="scoreboard",
            name="junior_score",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="scoreboard",
            name="senior_score",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="scoreboard",
            name="sophomore_score",
            field=models.IntegerField(default=0),
        ),
    ]
