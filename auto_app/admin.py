from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Car)
admin.site.register(models.AutoPartsType)
admin.site.register(models.AutoParts)
admin.site.register(models.AutoPartsWarehouse)

