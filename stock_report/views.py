from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from . import forms
from .models import AutoPartsWarehouse

def form(request):
    form_from_car = forms.CarForm
    form_from_auto_parts_type = forms.AutoPartsTypeForm
    form_from_auto_parts = forms.AutoPartsForm
    form_from_auto_parts_warehouse = forms.AutoPartsWarehouseForm
    context = {
        "form_from_car": form_from_car,
        "form_from_auto_parts_type": form_from_auto_parts_type,
        "form_from_auto_parts": form_from_auto_parts,
        "form_from_auto_parts_warehouse": form_from_auto_parts_warehouse,
    }

    return render(request, "index.html", context)

def add_car(request):
    form_from_car = forms.CarForm
    form_from_auto_parts_type = forms.AutoPartsTypeForm
    form_from_auto_parts = forms.AutoPartsForm
    form_from_auto_parts_warehouse = forms.AutoPartsWarehouseForm

    form = forms.CarForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            data = form.cleaned_data
            form.save()

            context = {
                "form_from_car": form_from_car,
                "form_from_auto_parts_type": form_from_auto_parts_type,
                "form_from_auto_parts": form_from_auto_parts,
                "form_from_auto_parts_warehouse": form_from_auto_parts_warehouse,
                "result_add_car": "Добавлено !",
            }

            return render(request, "index.html", context)

def add_auto_parts_type(request):
    form_from_car = forms.CarForm
    form_from_auto_parts_type = forms.AutoPartsTypeForm
    form_from_auto_parts = forms.AutoPartsForm
    form_from_auto_parts_warehouse = forms.AutoPartsWarehouseForm

    form = forms.AutoPartsTypeForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            data = form.cleaned_data
            form.save()

            context = {
                "form_from_car": form_from_car,
                "form_from_auto_parts_type": form_from_auto_parts_type,
                "form_from_auto_parts": form_from_auto_parts,
                "form_from_auto_parts_warehouse": form_from_auto_parts_warehouse,
                "result_add_auto_parts_type": "Добавлено !",
            }

            return render(request, "index.html", context)

def add_auto_parts(request):
    form_from_car = forms.CarForm
    form_from_auto_parts_type = forms.AutoPartsTypeForm
    form_from_auto_parts = forms.AutoPartsForm
    form_from_auto_parts_warehouse = forms.AutoPartsWarehouseForm

    form = forms.AutoPartsForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            data = form.cleaned_data
            form.save()

            context = {
                "form_from_car": form_from_car,
                "form_from_auto_parts_type": form_from_auto_parts_type,
                "form_from_auto_parts": form_from_auto_parts,
                "form_from_auto_parts_warehouse": form_from_auto_parts_warehouse,
                "result_add_auto_parts": "Добавлено !",
            }

            return render(request, "index.html", context)

def add_auto_parts_warehouse(request):
    form_from_car = forms.CarForm
    form_from_auto_parts_type = forms.AutoPartsTypeForm
    form_from_auto_parts = forms.AutoPartsForm
    form_from_auto_parts_warehouse = forms.AutoPartsWarehouseForm

    form = forms.AutoPartsWarehouseForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            data = form.cleaned_data
            form.save()

            context = {
                "form_from_car": form_from_car,
                "form_from_auto_parts_type": form_from_auto_parts_type,
                "form_from_auto_parts": form_from_auto_parts,
                "form_from_auto_parts_warehouse": form_from_auto_parts_warehouse,
                "result_add_auto_parts_warehouse": "Добавлено !",
            }

            return render(request, "index.html", context)

class List(TemplateView):
    template_name = 'warehouse.html'
    def get(self, request):
        all_parts = AutoPartsWarehouse.objects.all()

        context = {
            'all_parts': all_parts,
        }
        return render(request, self.template_name, context)
    def post(self, request):
        pass