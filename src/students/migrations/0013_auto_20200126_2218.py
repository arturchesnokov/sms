# Generated by Django 2.2.9 on 2020-01-26 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0012_auto_20200126_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='telephone',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]