from django.conf.urls import include, url
from django.contrib import admin, auth
from sandbox import settings


urlpatterns = [
    # Examples:
    # url(r'^$', 'sandbox.views.home', name='home'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('metaord.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]