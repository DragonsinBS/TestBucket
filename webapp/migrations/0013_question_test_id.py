# Generated by Django 2.2.5 on 2019-10-29 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0012_test_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='test_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='webapp.Test'),
        ),
    ]
