from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^orders/$', views.orders_list, name='orders_list'),
    url(r'^order/(?P<order_id>[0-9]+)/$', views.order, name='order'),
]
