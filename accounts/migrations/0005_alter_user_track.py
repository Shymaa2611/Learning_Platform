# Generated by Django 4.1.10 on 2023-08-30 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_skills'),
        ('accounts', '0004_profile_level_profile_skill_profile_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='track',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.track'),
        ),
    ]