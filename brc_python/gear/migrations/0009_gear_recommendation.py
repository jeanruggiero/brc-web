# Generated by Django 3.0.2 on 2020-01-26 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gear', '0008_auto_20200126_1932'),
    ]

    operations = [
        migrations.AddField(
            model_name='gear',
            name='recommendation',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
