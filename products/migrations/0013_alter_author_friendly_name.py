# Generated by Django 4.2.8 on 2024-11-09 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_alter_author_friendly_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='friendly_name',
            field=models.CharField(max_length=254),
        ),
    ]