# Generated by Django 4.1.10 on 2023-09-01 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_skills'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['id']},
        ),
    ]
