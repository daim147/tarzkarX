# Generated by Django 2.2.10 on 2021-10-31 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20211031_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcolor',
            name='color',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='productcolor',
            name='name',
            field=models.CharField(max_length=64),
        ),
    ]
