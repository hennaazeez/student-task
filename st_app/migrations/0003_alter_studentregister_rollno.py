# Generated by Django 4.1.7 on 2023-03-19 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('st_app', '0002_studentregister'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentregister',
            name='rollno',
            field=models.IntegerField(max_length=6),
        ),
    ]