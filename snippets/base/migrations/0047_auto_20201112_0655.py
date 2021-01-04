# Generated by Django 2.2.13 on 2020-11-12 06:55

from django.db import migrations, models
import snippets.base.validators


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0046_auto_20201027_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='target',
            name='jexl_expr',
            field=models.TextField(blank=True, default='', validators=[snippets.base.validators.validate_jexl]),
        ),
    ]