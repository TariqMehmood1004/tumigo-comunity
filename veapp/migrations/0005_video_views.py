# Generated by Django 4.2.5 on 2024-01-06 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veapp', '0004_video_channel_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
