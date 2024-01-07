# Generated by Django 4.2.5 on 2024-01-07 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veapp', '0008_video_channel_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='video',
            name='tags',
            field=models.CharField(default='', max_length=255),
        ),
    ]