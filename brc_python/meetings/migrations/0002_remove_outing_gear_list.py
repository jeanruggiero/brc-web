# Generated by Django 3.0 on 2020-01-25 02:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='outing',
            name='gear_list',
        ),
    ]