# Generated by Django 2.1.8 on 2019-10-11 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('balance_scorecard', '0033_acumulado_kpi_meta_mensual'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acumulado_kpi',
            name='meta_mensual',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
