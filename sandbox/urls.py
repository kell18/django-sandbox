from django.conf.urls import include, url
from django.contrib import admin, auth


urlpatterns = [
    # Examples:
    # url(r'^$', 'sandbox.views.home', name='home'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('metaord.urls')),
]
