from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main),
    url(r'^test$', views.test),
    url(r'^register$', views.register),
    url(r'^success/(?P<userID>\d+)$', views.success),
    url(r'^login$', views.login),
]