# Generated by Django 4.1.10 on 2023-08-30 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_skills'),
        ('accounts', '0003_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='level',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='pages.levels'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='skill',
            field=models.ManyToManyField(to='pages.skills'),
        ),
        migrations.AddField(
            model_name='profile',
            name='task',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='pages.task'),
            preserve_default=False,
        ),
    ]