# Generated by Django 3.1.7 on 2021-10-17 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crime', '0010_auto_20211011_2236'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='ribstation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crime.ribstation'),
        ),
    ]