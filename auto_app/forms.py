from django import forms
from django.forms import ModelForm
from . import models
from django.utils.safestring import mark_safe
from .models import AutoPartsWarehouse
from .models import AutoParts
from .models import AutoPartsType
from .models import Car


class CarForm(forms.ModelForm):
    car_brand = forms.CharField(label= mark_safe("Марка автомобіля"), widget=forms.TextInput(attrs={'class': 'myfield', 'name':'car_brand'}))
    car_model = forms.CharField(label= mark_safe("Модель автомобіля"),
                    widget=forms.TextInput(attrs={'class': 'myfield', 'name': 'car_brand'}))
    car_year = forms.IntegerField(label=mark_safe("Рік випуску"),
                                  widget=forms.TextInput(attrs={'class': 'myfield', 'name': 'car_brand', 'type':'number'}))
    class Meta:
        model = Car
        field = ["car_brand", "car_model", "car_year"]
        exclude = ()

class AutoPartsTypeForm(forms.ModelForm):
    parts_type =  forms.CharField(label= "Тип автозапзастини", widget=forms.TextInput(attrs={'class': 'myfield', 'name':'car_brand'}))
    class Meta:
        model = AutoPartsType
        field = ["parts_type"]
        exclude = ()

class AutoPartsForm(forms.ModelForm):
    parts_name =  forms.CharField(label= "Назва автозапзастини", widget=forms.TextInput(attrs={'class': 'myfield', 'name':'car_brand'}))

    class Meta:
        model = AutoParts
        field = ["parts_name", "car_model", "part_type"]
        exclude = ()

class AutoPartsWarehouseForm(forms.ModelForm):
    numbers_of_pats  = forms.IntegerField(label=mark_safe("Кількість запчастей"),
                                  widget=forms.TextInput(attrs={'class': 'myfield', 'name': 'car_brand', 'type':'number'}))
    price_of_parts = forms.IntegerField(label=mark_safe("Ціна 1й запчастини"),
                                  widget=forms.TextInput(attrs={'class': 'myfield', 'name': 'car_brand', 'type':'number'}))
    class Meta:
        model = AutoPartsWarehouse
        field = ["parts_name_warehouse", "numbers_of_pats", "price_of_parts"]
        exclude = ()