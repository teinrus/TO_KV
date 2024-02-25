# Generated by Django 5.0.2 on 2024-02-24 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_TO', '0002_remove_task_photo_alter_task_status_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='line',
            field=models.CharField(choices=[('24', '24'), ('25', '25'), ('26', '26'), ('31', '31'), ('33', '33')], default='31', max_length=20),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('Не решена', 'Не решена'), ('Принята', 'Принята'), ('Выполнено', 'Выполнено')], default='Не решена', max_length=20),
        ),
    ]