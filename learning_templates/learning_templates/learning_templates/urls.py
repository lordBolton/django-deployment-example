"""
Definition of urls for learning_templates.
"""

from django.conf.urls import include, url
from basic_app import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', learning_templates.views.home, name='home'),
    # url(r'^learning_templates/', include('learning_templates.learning_templates.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^basic_app/', include('basic_app.urls')),

]
