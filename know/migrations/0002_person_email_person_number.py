# Generated by Django 4.2.3 on 2023-08-03 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('know', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='email',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AddField(
            model_name='person',
            name='number',
            field=models.CharField(default='', max_length=10),
        ),
    ]
