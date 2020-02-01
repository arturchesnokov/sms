# Generated by Django 2.2.9 on 2020-01-31 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0013_auto_20200126_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='is_enabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.CharField(default='111111', max_length=25),
        ),
        migrations.AddField(
            model_name='student',
            name='username',
            field=models.CharField(default='', max_length=25, unique=True),
        ),
    ]
