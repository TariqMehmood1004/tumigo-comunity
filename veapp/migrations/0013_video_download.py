# Generated by Django 4.2.5 on 2024-01-07 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veapp', '0012_video_dislikes'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='download',
            field=models.BooleanField(default=False),
        ),
    ]
