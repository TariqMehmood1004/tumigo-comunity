# Generated by Django 4.2.5 on 2024-01-07 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veapp', '0011_alter_video_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='disLikes',
            field=models.IntegerField(default=0),
        ),
    ]
