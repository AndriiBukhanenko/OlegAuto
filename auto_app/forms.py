from django import forms
from django.forms import ModelForm
from . import models
from django.utils.safestring import mark_safe
from .models import AutoPartsWarehouse
from .models import AutoParts
from .models import AutoPartsType
from .models import Car


class CarForm(forms.ModelForm):
    car_brand = forms.CharField(label= mark_safe("<strong>Марка автомобиля</strong>"), widget=forms.TextInput(attrs={'class': 'myfield', 'name':'car_brand'}))
    car_model = forms.CharField(label=mark_safe("<strong>Модель автомобиля</strong>"),
                    widget=forms.TextInput(attrs={'class': 'myfield', 'name': 'car_brand'}))
    car_year = forms.IntegerField(label=mark_safe("<strong>Год выпуска</strong>"), widget=forms.TextInput(attrs={'class': 'myfield', 'name': 'car_brand'}))
    class Meta:
        model = Car
        field = ["car_brand", "car_model", "car_year"]
        exclude = ()

class AutoPartsTypeForm(forms.ModelForm):
    class Meta:
        model = AutoPartsType
        field = ["parts_type"]
        exclude = ()

class AutoPartsForm(forms.ModelForm):
    class Meta:
        model = AutoParts
        field = ["parts_name", "car_model", "part_type"]
        exclude = ()

class AutoPartsWarehouseForm(forms.ModelForm):
    class Meta:
        model = AutoPartsWarehouse
        field = ["parts_name", "numbers_of_pats", "price_of_parts"]
        exclude = ()