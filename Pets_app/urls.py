from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^/pets/create$', views.index),
    url(r'pets/delete/(?P<getUserID>\d+)', views.deletePet),
}

