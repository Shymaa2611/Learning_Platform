# Generated by Django 4.1.10 on 2023-09-06 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_alter_blog_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='poster',
            field=models.ImageField(default='', upload_to='video/poster/'),
            preserve_default=False,
        ),
    ]