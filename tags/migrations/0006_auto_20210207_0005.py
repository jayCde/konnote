# Generated by Django 3.0.8 on 2021-02-07 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0005_auto_20210207_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(default=' ', unique=True),
        ),
    ]