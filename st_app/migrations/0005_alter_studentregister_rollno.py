# Generated by Django 4.1.7 on 2023-03-21 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('st_app', '0004_notification_complaint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentregister',
            name='rollno',
            field=models.IntegerField(),
        ),
    ]
