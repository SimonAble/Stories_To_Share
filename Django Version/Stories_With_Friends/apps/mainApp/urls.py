from django.conf.urls import url
from . import views

urlpatterns = [

    #HOME PAGE ROUTING
    url(r'^$', views.index),
    url(r'^home$', views.index),

    #MAIN WRITING ROUTES
    url(r'^write$', views.write),

    #MAIN WRITING ROUTES
    url(r'^explore$', views.explore),

    #MAIN WRITING ROUTES
    url(r'^profile/userid$', views.profile),

    #LOGIN/LOGOUT ROUTING
    url(r'^login$', views.login),

]