# Generated by Django 4.2.5 on 2024-01-07 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veapp', '0014_remove_video_download_video_downloads_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='disLikes',
        ),
        migrations.RemoveField(
            model_name='video',
            name='downloads',
        ),
        migrations.AddField(
            model_name='video',
            name='download',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userinteraction',
            name='likes',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='video',
            name='comments',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='video',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='video',
            name='shares',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='video',
            name='views',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='video',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
    ]
