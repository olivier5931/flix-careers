# Generated by Django 5.0.2 on 2024-03-02 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0003_jobpost_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='slug',
            field=models.SlugField(max_length=40, null=True, unique=True),
        ),
    ]
