from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from . import forms
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.utils.safestring import mark_safe
from .models import AutoPartsWarehouse
from .models import AutoParts

def start_page(request):
    return render(request, "index.html")

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

    return render(request, "add_new.html", context)


def add_car_view(request):
    form_from_car = forms.CarForm
    context = {
        "form_from_car": form_from_car,
    }
    return render(request, "add_car.html", context)

def add_car(request):
    form_from_car = forms.CarForm
    form = forms.CarForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            data = form.cleaned_data
            form.save()

            context = {
                "form_from_car": form_from_car,
                "result_add_car":  mark_safe("<strong>Добавлено !</strong>"),
            }

            return render(request, "add_car.html", context)


def add_auto_parts_type_view(request):
    form_from_auto_parts_type = forms.AutoPartsTypeForm
    context = {
        "form_from_auto_parts_type": form_from_auto_parts_type,
    }

    return render(request, "add_auto_parts_type.html", context)

def add_auto_parts_type(request):
    form_from_auto_parts_type = forms.AutoPartsTypeForm
    form = forms.AutoPartsTypeForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            data = form.cleaned_data
            form.save()

            context = {
                "form_from_auto_parts_type": form_from_auto_parts_type,
                "result_add_auto_parts_type":  mark_safe("<strong>Добавлено !</strong>"),
            }

            return render(request, "add_auto_parts_type.html", context)


def add_auto_parts_view(request):
    form_from_auto_parts = forms.AutoPartsForm
    context = {
        "form_from_auto_parts": form_from_auto_parts,
    }

    return render(request, "add_auto_parts.html", context)

def add_auto_parts(request):
    form_from_auto_parts = forms.AutoPartsForm
    form = forms.AutoPartsForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            data = form.cleaned_data
            form.save()

            context = {
                "form_from_auto_parts": form_from_auto_parts,
                "result_add_auto_parts":  mark_safe("<strong>Добавлено !</strong>"),
            }

            return render(request, "add_auto_parts.html", context)



def add_auto_parts_warehouse_view(request):
    form_from_auto_parts_warehouse = forms.AutoPartsWarehouseForm
    context = {
        "form_from_auto_parts_warehouse": form_from_auto_parts_warehouse,
    }

    return render(request, "add_auto_parts_warehouse.html", context)

def add_auto_parts_warehouse(request):
    form_from_auto_parts_warehouse = forms.AutoPartsWarehouseForm
    form = forms.AutoPartsWarehouseForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            data = form.cleaned_data
            form.save()

            context = {
                "form_from_auto_parts_warehouse": form_from_auto_parts_warehouse,
                "result_add_auto_parts_warehouse":  mark_safe("<strong>Добавлено !</strong>"),
            }

            return render(request, "add_auto_parts_warehouse.html", context)

class List(TemplateView):
    template_name = 'warehouse.html'
    def get(self, request):
        all_parts = AutoPartsWarehouse.objects.all()

        context = {
            'all_parts': all_parts,
        }
        return render(request, self.template_name, context)
    def post(self, request):
        query = request.POST['search']

        result_list =AutoPartsWarehouse.objects.filter(AutoParts__parts_name= AutoPartsWarehouse.parts_name_warehouse)
        if result_list.count() != 0:
            context = {
                "all_parts": result_list,
                "query": query,
            }
        else:
            context = {
                "empty":  mark_safe("<strong>Ничего не найдено !</strong>"),
                "query": query,

            }
        return render(request, self.template_name, context)


def edit(request, id):
    try:
        parts = AutoPartsWarehouse.objects.get(parts_name_warehouse_id=id)

        if request.method == "POST":
            parts.numbers_of_pats = request.POST.get("numbers_of_pats")
            parts.price_of_parts = request.POST.get("price_of_parts")
            parts.save()

            return HttpResponseRedirect("/list/")
        else:
            return render(request, "edit.html", {"parts": parts})
    except AutoPartsWarehouse.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")

def delete(request, id):
    try:
        person = AutoPartsWarehouse.objects.get(parts_name_warehouse_id=id)
        person.delete()
        return HttpResponseRedirect("/list/")
    except AutoPartsWarehouse.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")