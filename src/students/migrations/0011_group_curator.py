# Generated by Django 2.2.9 on 2020-01-19 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_auto_20200119_1711'),
        ('students', '0010_group_praepostor'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='curator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='teachers.Teacher'),
        ),
    ]