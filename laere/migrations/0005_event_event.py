# Generated by Django 4.0.6 on 2022-07-23 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laere', '0004_alter_event_photo_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
