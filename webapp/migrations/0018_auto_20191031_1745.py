# Generated by Django 2.2.5 on 2019-10-31 12:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0017_auto_20191031_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='test',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 10, 31, 12, 15, 15, 323879, tzinfo=utc)),
        ),
    ]