# Generated by Django 3.2.10 on 2023-03-07 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_item_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='slug',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]