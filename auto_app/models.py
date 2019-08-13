from django.db import models
from django.utils.safestring import mark_safe
# Create your models here.


class Car(models.Model):
    car_brand = models.CharField(max_length=200, verbose_name="Марка автомобиля")
    car_model = models.CharField(max_length=200, verbose_name="Модель автомобиля")
    car_year = models.IntegerField(verbose_name="Год выпуска")

    def __str__(self):
        return self.car_brand.title()+" "+self.car_model.title()+" "+str(self.car_year)

class AutoPartsType(models.Model):
    parts_type = models.CharField(max_length=200, verbose_name="Тип автозапчасти")

    def __str__(self):
        return str(self.parts_type.title())

class AutoParts(models.Model):
    parts_name = models.CharField(max_length=200, verbose_name="Название автозапчасти")
    car_model = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name="Модель автомобиля")
    parts_type = models.ForeignKey(AutoPartsType, on_delete=models.CASCADE, verbose_name="Тип автозапчасти")

    def __str__(self):
        return self.parts_name.title()+" ("+ str(self.parts_type.parts_type.title())+" | "+self.car_model.car_brand.title()+" "\
               + self.car_model.car_model+" "+str(self.car_model.car_year) +")"

class AutoPartsWarehouse(models.Model):
    parts_name_warehouse = models.OneToOneField(AutoParts, on_delete=models.CASCADE, related_name='profile', primary_key=True,
                                      verbose_name="Название автозапчасти")
    numbers_of_pats = models.PositiveIntegerField(verbose_name="Количество запчастей")
    price_of_parts = models.PositiveIntegerField(verbose_name="Цена 1й запчати")

    def __str__(self):
        return self.parts_name_warehouse.parts_name.title()+" ("+ str(self.parts_name_warehouse.parts_type.parts_type.title())+" | "+self.parts_name_warehouse.car_model.car_brand.title()+" "\
               + self.parts_name_warehouse.car_model.car_model+" "+str(self.parts_name_warehouse.car_model.car_year) +")"+" : "+str(self.numbers_of_pats)+"шт., "+str(self.price_of_parts)+" DKK"


