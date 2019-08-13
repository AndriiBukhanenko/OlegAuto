# Generated by Django 2.2.3 on 2019-08-12 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auto_app', '0005_auto_20190812_2140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autoparts',
            name='id',
        ),
        migrations.AlterField(
            model_name='autoparts',
            name='parts_name',
            field=models.CharField(max_length=200, primary_key=True, serialize=False, verbose_name='Название автозапчасти'),
        ),
        migrations.AlterField(
            model_name='autopartswarehouse',
            name='parts_name_warehouse',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profile', serialize=False, to='auto_app.AutoParts', verbose_name='Название автозапчасти'),
        ),
    ]
