# Generated by Django 5.0.2 on 2024-02-24 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_TO', '0004_task_shift_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='shift_name',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], default='1', max_length=2),
        ),
    ]
