# Generated by Django 2.2.3 on 2019-07-19 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock_report', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AutoParts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parts_name', models.CharField(max_length=30)),
                ('car_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock_report.Car')),
            ],
        ),
        migrations.CreateModel(
            name='AutoPartsType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parts_type', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='AutoPartsWarehouse',
            fields=[
                ('parts_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='stock_report.AutoParts')),
                ('numbers_of_pats', models.PositiveIntegerField()),
                ('price_of_parts', models.PositiveIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='autoparts',
            name='part_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock_report.AutoPartsType'),
        ),
    ]
