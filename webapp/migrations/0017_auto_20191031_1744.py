# Generated by Django 2.2.5 on 2019-10-31 12:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0016_auto_20191031_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='teacher_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='test',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 10, 31, 12, 14, 42, 215321, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='test',
            name='test_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]