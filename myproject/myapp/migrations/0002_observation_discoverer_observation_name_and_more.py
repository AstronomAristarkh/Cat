# Generated by Django 5.0.7 on 2024-08-17 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='observation',
            name='discoverer',
            field=models.CharField(default=None, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='observation',
            name='name',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='observation',
            name='sattelite',
            field=models.CharField(max_length=30),
        ),
    ]
