# Generated by Django 3.1.7 on 2021-10-10 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crime', '0003_auto_20211010_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='case_desc',
            field=models.TextField(),
        ),
    ]
