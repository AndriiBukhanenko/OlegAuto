from django.db import models

# Create your models here.


class Car(models.Model):
    car_brand = models.CharField(max_length=200, verbose_name="Марка автомобиля")
    car_model = models.CharField(max_length=200, verbose_name="Модель автомобиля")
    car_year = models.DateField(verbose_name="Год выпуска")

class AutoPartsType(models.Model):
    parts_type = models.CharField(max_length=200, verbose_name="Тип автозапчасти")

class AutoParts(models.Model):
    parts_name = models.CharField(max_length=200, verbose_name="Название автозапчасти")
    car_model = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name="Модель автомобиля")
    part_type = models.ForeignKey(AutoPartsType, on_delete=models.CASCADE, verbose_name="Тип автозапчасти")

class AutoPartsWarehouse(models.Model):
    parts_name = models.OneToOneField(AutoParts, on_delete=models.CASCADE, primary_key=True,
                                      verbose_name="Название автозапчасти")
    numbers_of_pats = models.PositiveIntegerField(verbose_name="Количество запчастей")
    price_of_parts = models.PositiveIntegerField(verbose_name="Цена 1й запчати")

