from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^dssh/', include('dssh.urls')),
    url(r'^$', include('dssh.urls')),
]
