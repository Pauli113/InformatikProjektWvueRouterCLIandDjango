# Generated by Django 4.0.6 on 2022-09-01 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_course_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='lecture',
            field=models.IntegerField(default=''),
        ),
    ]
