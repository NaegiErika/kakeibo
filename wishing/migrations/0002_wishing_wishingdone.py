# Generated by Django 3.0.3 on 2020-02-12 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishing',
            name='wishingdone',
            field=models.BooleanField(default=False, verbose_name='達成状況'),
            preserve_default=False,
        ),
    ]