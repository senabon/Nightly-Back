# Generated by Django 4.0.6 on 2022-07-23 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laere', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='dateTime',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
