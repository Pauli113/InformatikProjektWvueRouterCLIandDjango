# Generated by Django 4.0.6 on 2022-09-02 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module_code', models.CharField(max_length=140)),
                ('module_title', models.CharField(max_length=140)),
                ('module_abbrev', models.CharField(max_length=140)),
                ('module_type', models.CharField(max_length=140)),
                ('credit_points', models.IntegerField()),
                ('language', models.CharField(max_length=140)),
                ('duration_of_module', models.IntegerField()),
                ('recommended_semester', models.IntegerField()),
                ('frequency', models.CharField(max_length=140)),
                ('coordinators', models.TextField(null=True)),
                ('lecturers', models.TextField(null=True)),
                ('assessment_method', models.CharField(default='', max_length=140)),
                ('workload', models.IntegerField()),
                ('seminar', models.IntegerField(default=0)),
                ('practical', models.IntegerField(default=0)),
                ('excercise', models.IntegerField(default=0)),
                ('self_study', models.IntegerField(default=0)),
                ('required_prerequisites', models.TextField(null=True)),
                ('recommended_prerequisites', models.TextField(null=True)),
                ('status', models.CharField(default='', max_length=140)),
                ('location', models.CharField(default='', max_length=140)),
                ('po', models.CharField(default='', max_length=140)),
                ('furtherInformation', models.CharField(default='', max_length=1000)),
            ],
        ),
    ]
