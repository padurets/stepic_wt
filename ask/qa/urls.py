from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.test),
    # url(r'^(?P<id>\d+)/$', views.test)
]
