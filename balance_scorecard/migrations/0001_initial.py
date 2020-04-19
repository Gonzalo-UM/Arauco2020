# Generated by Django 2.2.2 on 2019-08-27 00:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Indicador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_kpi', models.CharField(max_length=200)),
                ('meta_kpi', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5000), django.core.validators.MinValueValidator(0)])),
                ('descripcion_kpi', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
