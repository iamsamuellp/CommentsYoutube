# Generated by Django 3.2.7 on 2021-09-19 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='first',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='last',
        ),
        migrations.AddField(
            model_name='comments',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comments',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comments',
            name='video_Id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
