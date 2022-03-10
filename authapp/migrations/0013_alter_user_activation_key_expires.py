# Generated by Django 3.2 on 2022-01-22 09:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0012_alter_user_activation_key_expires'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 1, 24, 9, 40, 40, 193345, tzinfo=utc), null=True),
        ),
    ]
