# Generated by Django 5.2.2 on 2025-06-11 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_alter_events_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='image',
        ),
    ]
