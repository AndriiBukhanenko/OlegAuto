from django.conf.urls import url
from . import views
from .views import List

urlpatterns = [

    url(r'^add-car/$', views.add_car),
    url(r'^add-auto-parts-type/$', views.add_auto_parts_type),
    url(r'^add-auto-parts/$', views.add_auto_parts),
    url(r'^add-auto-parts-warehouse/$', views.add_auto_parts_warehouse),
    #url(r'', views.form),
    url(r'', List.as_view(), name=';ist-view'),
]


