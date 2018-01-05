
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^reset', views.reset),
    url(r'^process_money/(?P<building>\w+)', views.process_money),
    url(r'^$', views.main),
]
