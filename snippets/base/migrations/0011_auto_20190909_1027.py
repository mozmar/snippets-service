# Generated by Django 2.2.3 on 2019-09-09 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_auto_20190905_1551'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job',
            options={'ordering': ['-modified']},
        ),
    ]
