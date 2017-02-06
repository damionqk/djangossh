from django.conf.urls import url
from . import views

app_name = 'dssh'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^sshl/$', views.cssh, name='cssh'),
]
