from django.conf.urls import include, url
from tasks import views

urlpatterns = [
    url(r'^$', views.all),
    url(r'^(?P<id>\d+)$', views.one),
]

