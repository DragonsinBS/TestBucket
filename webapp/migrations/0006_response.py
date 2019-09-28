# Generated by Django 2.2.5 on 2019-09-24 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Response', models.CharField(choices=[('A', 'Option A'), ('B', 'Option B'), ('C', 'Option C'), ('D', 'Option D')], max_length=1)),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Question')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Student')),
                ('test_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Test')),
            ],
            options={
                'unique_together': {('student_id', 'test_id')},
            },
        ),
    ]
