# Generated by Django 4.2.8 on 2023-12-31 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_user_event_list_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_list',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
