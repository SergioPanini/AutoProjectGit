# Generated by Django 3.0.2 on 2020-03-23 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200323_1332'),
    ]

    operations = [
        migrations.RenameField(
            model_name='numbers',
            old_name='CarNuber',
            new_name='CarNumber',
        ),
    ]