# Generated by Django 3.0.2 on 2020-03-23 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200323_1205'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cards',
        ),
        migrations.DeleteModel(
            name='CarNumbers',
        ),
    ]