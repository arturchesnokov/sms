# Generated by Django 2.2.9 on 2020-01-03 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_student_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
            ],
        ),
    ]
