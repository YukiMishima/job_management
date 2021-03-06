# Generated by Django 2.2.3 on 2019-07-17 02:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='名前')),
                ('support', models.IntegerField(choices=[(1, 'anatase'), (2, 'rutile')], default=1, verbose_name='担体')),
                ('memo', models.TextField(blank=True, max_length=500, null=True, verbose_name='備考')),
                ('send_date', models.DateField(default=django.utils.timezone.now, verbose_name='投げた日')),
                ('get_date', models.DateField(blank=True, null=True, verbose_name='返ってきた日')),
            ],
            options={
                'verbose_name': 'アイテム',
                'verbose_name_plural': 'アイテム',
            },
        ),
    ]
