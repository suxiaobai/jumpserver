# Generated by Django 2.1.7 on 2020-05-19 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ops', '0009_auto_20200515_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskargument',
            name='name',
            field=models.CharField(max_length=128, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='taskexecution',
            name='execute_user',
            field=models.CharField(blank=True, default='system', max_length=128),
        ),
        migrations.AlterField(
            model_name='taskexecution',
            name='task_meta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_execution', to='ops.TaskMeta'),
        ),
    ]
