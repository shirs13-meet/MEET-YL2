from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
url(r'^Thanks/$', views.Thanks, name="Thanks"),
url(r'^contact/$', views.contact, name="contact"),
url(r'^homepage/$', views.homepage, name="homepage"),

)
