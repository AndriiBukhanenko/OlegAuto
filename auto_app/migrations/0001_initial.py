# Generated by Django 2.2.3 on 2019-08-10 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AutoParts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parts_name', models.CharField(max_length=200, verbose_name='Название автозапчасти')),
            ],
        ),
        migrations.CreateModel(
            name='AutoPartsType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parts_type', models.CharField(max_length=200, verbose_name='Тип автозапчасти')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_brand', models.CharField(max_length=200, verbose_name='Марка автомобиля')),
                ('car_model', models.CharField(max_length=200, verbose_name='Модель автомобиля')),
                ('car_year', models.IntegerField(verbose_name='Год выпуска')),
            ],
        ),
        migrations.CreateModel(
            name='AutoPartsWarehouse',
            fields=[
                ('parts_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auto_app.AutoParts', verbose_name='Название автозапчасти')),
                ('numbers_of_pats', models.PositiveIntegerField(verbose_name='Количество запчастей')),
                ('price_of_parts', models.PositiveIntegerField(verbose_name='Цена 1й запчати')),
            ],
        ),
        migrations.AddField(
            model_name='autoparts',
            name='car_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auto_app.Car', verbose_name='Модель автомобиля'),
        ),
        migrations.AddField(
            model_name='autoparts',
            name='part_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auto_app.AutoPartsType', verbose_name='Тип автозапчасти'),
        ),
    ]