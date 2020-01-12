# Generated by Django 2.2.9 on 2020-01-03 09:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('students', '0003_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='group',
            name='students_count',
            field=models.IntegerField(default=0),
        ),
    ]
