from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^user/login/$', auth_views.login, name='login'),
    url(r'^user/logout/$', auth_views.logout, name='logout', kwargs={'next_page': '/'}),

    url(r'^user/register_operator$', views.register_operator_form, name='register_operator_form'),
    url(r'^user/register_operator_submit$', views.register_operator_submit, name='register_operator_submit'),

    url(r'^orders/$', views.orders_list, name='orders_list'),
    url(r'^order/(?P<order_id>[0-9]+)/$', views.order, name='order'),
]
