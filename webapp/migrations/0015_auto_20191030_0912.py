# Generated by Django 2.2.5 on 2019-10-30 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0014_auto_20191029_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='score',
            field=models.IntegerField(choices=[(0, 0), (1, 1)]),
        ),
    ]
