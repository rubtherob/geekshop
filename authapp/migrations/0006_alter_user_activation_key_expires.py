# Generated by Django 3.2 on 2021-12-21 13:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0005_alter_user_activation_key_expires'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 12, 23, 13, 51, 57, 785903, tzinfo=utc), null=True),
        ),
    ]
