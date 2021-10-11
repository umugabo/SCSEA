# Generated by Django 3.1.7 on 2021-10-10 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crime', '0005_auto_20211010_1553'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evidence',
            name='suspect',
        ),
        migrations.AddField(
            model_name='suspect',
            name='evidences',
            field=models.ManyToManyField(blank=True, null=True, to='crime.Evidence'),
        ),
    ]
