from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^login/$', views.LoginFormView.as_view()),
    #url(r'^logout/$',views.LogoutFormView.as_view()),
    url(r'^$',views.start_page),
    url(r'^login/$', views.login_view),
    url(r'^logout/$', views.logout_view),
]


