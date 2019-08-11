from django.conf.urls import url
from . import views
from .views import List

urlpatterns = [
    url(r'^list/$', List.as_view(), name='List-view'),
    url(r'form/$', views.form),
    url(r'add-car-view/$', views.add_car_view),
    url(r'add-car/$', views.add_car),
    url(r'^add-auto-parts-type/$', views.add_auto_parts_type),
    url(r'^add-auto-parts/$', views.add_auto_parts),
    url(r'^add-auto-parts-warehouse/$', views.add_auto_parts_warehouse),
    url(r'^$',views.start_page),

]


