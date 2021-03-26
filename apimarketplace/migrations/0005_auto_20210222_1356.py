# Generated by Django 3.1.6 on 2021-02-22 16:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apimarketplace', '0004_auto_20210222_0946'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='password',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='data',
            field=models.DateField(default=datetime.datetime(2021, 2, 22, 13, 56, 39, 8826)),
        ),
    ]
