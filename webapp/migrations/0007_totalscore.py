# Generated by Django 2.2.5 on 2019-09-24 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_response'),
    ]

    operations = [
        migrations.CreateModel(
            name='TotalScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_marks', models.IntegerField(default=0)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Student')),
                ('test_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Test')),
            ],
            options={
                'unique_together': {('student_id', 'test_id')},
            },
        ),
    ]
