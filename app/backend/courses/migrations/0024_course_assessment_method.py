# Generated by Django 4.0.6 on 2022-09-02 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0023_course_lecturers'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='assessment_method',
            field=models.CharField(default='', max_length=140),
        ),
    ]
