# Generated by Django 3.0.3 on 2020-02-25 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messenger_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['time_create'], 'verbose_name': 'Message', 'verbose_name_plural': 'Messages'},
        ),
    ]
