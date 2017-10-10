from django.conf.urls import url

from polls import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'(?P<q_id>\d+)/$', views.detail, name='detail'),
    url(r'(?P<q_id>\d+)/vote/$', views.vote, name='vote'),
    url(r'(?P<q_id>\d+)/result/$', views.result, name='result'),
    url(r'(?P<q_id>\d+)/result/revote/$', views.revote, name='revote')
]