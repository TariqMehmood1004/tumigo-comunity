# Generated by Django 4.2.5 on 2024-01-07 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veapp', '0009_video_description_video_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='descriptionHeading',
            field=models.CharField(default='', max_length=255),
        ),
    ]
