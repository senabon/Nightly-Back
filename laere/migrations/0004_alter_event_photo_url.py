# Generated by Django 4.0.6 on 2022-07-23 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laere', '0003_event_photo_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='photo_url',
            field=models.CharField(max_length=600, null=True),
        ),
    ]
