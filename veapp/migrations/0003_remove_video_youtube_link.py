# Generated by Django 4.2.5 on 2024-01-06 00:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('veapp', '0002_video_embed_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='youtube_link',
        ),
    ]