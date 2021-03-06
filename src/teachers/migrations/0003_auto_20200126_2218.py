# Generated by Django 2.2.9 on 2020-01-26 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_auto_20200119_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='telephone',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]
