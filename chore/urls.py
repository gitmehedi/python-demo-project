from django.conf.urls import url

from . import views

urlpatterns = [
     url(r'^$', views.index, name='index'),
     url(r'^home/$', views.home, name='home'),
     url(r'^aboutus/$', views.aboutus, name='aboutus'),
     url(r'^service/$', views.service, name='service'),
     url(r'^bandwidth/$', views.bandwidth, name='bandwidth'),
     url(r'^software/$', views.software, name='software'),
     url(r'^contactus/$', views.contactus, name='contactus'),
]
