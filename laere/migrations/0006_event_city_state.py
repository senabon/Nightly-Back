# Generated by Django 4.0.6 on 2022-07-23 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laere', '0005_event_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='city_state',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
