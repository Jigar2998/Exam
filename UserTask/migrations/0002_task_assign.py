# Generated by Django 3.1.5 on 2021-03-23 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UserTask', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='task_assign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=25)),
                ('task_detail', models.CharField(max_length=25)),
                ('status', models.CharField(choices=[('Working', 'Working'), ('Working Done', 'Working Done')], default='Working', max_length=25)),
                ('assign_work_date', models.DateField(auto_now=True)),
                ('due_date', models.DateField()),
                ('assign_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserTask.user')),
            ],
        ),
    ]