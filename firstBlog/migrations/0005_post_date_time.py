# Generated by Django 5.1.6 on 2025-02-12 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstBlog', '0004_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
