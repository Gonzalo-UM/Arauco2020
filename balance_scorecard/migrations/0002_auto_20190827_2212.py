# Generated by Django 2.1.8 on 2019-08-28 02:12

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('balance_scorecard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acumulado_kpi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(null=True)),
                ('acumulado', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Info_kpi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_kpi', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(200), django.core.validators.MinValueValidator(0)])),
                ('fecha_modificacion', models.DateField(verbose_name=['%d/%m/%Y'])),
                ('indicador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='balance_scorecard.Indicador')),
            ],
        ),
        migrations.AddField(
            model_name='acumulado_kpi',
            name='valor_kpi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='balance_scorecard.Info_kpi'),
        ),
    ]
