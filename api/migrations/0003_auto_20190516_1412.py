# Generated by Django 2.2.1 on 2019-05-16 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190516_1308'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exercise',
            old_name='userid',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': 'username taken.'}, max_length=100, unique=True),
        ),
    ]
