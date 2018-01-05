
from django.conf.urls import url
from . import views
# from django.contrib import admin

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^generate$', views.generate),
    url(r'^reset$', views.reset),
    url(r'^', views.index),

]


