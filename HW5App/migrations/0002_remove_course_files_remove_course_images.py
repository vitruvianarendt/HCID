# Generated by Django 4.0.5 on 2022-07-02 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HW5App', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='files',
        ),
        migrations.RemoveField(
            model_name='course',
            name='images',
        ),
    ]