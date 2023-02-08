# Generated by Django 3.2.16 on 2023-01-29 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0136_remove_zombie_editorials'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='site_theme',
            field=models.CharField(choices=[('auto', 'Follow system default'), ('light', 'Light'), ('dark', 'Dark')], default='auto', max_length=10, verbose_name='site theme'),
        ),
    ]