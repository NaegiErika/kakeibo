# Generated by Django 3.0.1 on 2020-03-06 09:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wishing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wishingdate', models.DateField(default=datetime.datetime.now, verbose_name='日付')),
                ('wishingmoney', models.IntegerField(help_text='単位は日本円', verbose_name='金額')),
                ('wishingmemo', models.CharField(max_length=500, verbose_name='メモ')),
                ('wishingdone', models.BooleanField(default=False, verbose_name='達成状況')),
            ],
            options={
                'verbose_name': 'ほしいもの',
                'verbose_name_plural': 'ほしいもの',
                'db_table': 'wishing',
            },
        ),
    ]
