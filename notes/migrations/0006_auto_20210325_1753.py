# Generated by Django 3.1.7 on 2021-03-25 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0005_auto_20210325_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='tag',
            field=models.CharField(max_length=200),
        ),
    ]