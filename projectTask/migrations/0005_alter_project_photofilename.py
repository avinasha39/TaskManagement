# Generated by Django 3.2 on 2021-05-01 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectTask', '0004_auto_20210501_0614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='photoFileName',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=''),
        ),
    ]
