# Generated by Django 5.0.2 on 2024-03-03 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0004_alter_jobpost_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='expiry',
            field=models.DateField(null=True),
        ),
    ]
