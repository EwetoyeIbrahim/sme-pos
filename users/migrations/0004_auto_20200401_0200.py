# Generated by Django 3.0.4 on 2020-04-01 01:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_customuser_is_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='right',
        ),
        migrations.DeleteModel(
            name='Right',
        ),
    ]
