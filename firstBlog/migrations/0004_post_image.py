# Generated by Django 5.1.6 on 2025-02-12 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstBlog', '0003_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='', upload_to='img/'),
        ),
    ]
