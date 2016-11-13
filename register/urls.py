from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.regist_data, name='regist_data'),
    url(r'^index/$', views.index, name='index'),
    url(r'^today/$', views.today, name='today'),
    url(r'^get_query/$', views.get_query, name='get_query'),
]