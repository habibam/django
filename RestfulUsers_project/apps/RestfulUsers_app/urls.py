from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Index),
    url(r'^users$', views.Index), ## GET show all users
    url(r'^users/new$', views.New), ## GET new user form
    url(r'^users/create$', views.CreateUser), ## POST create new user
    url(r'^users/(?P<userID>\d+)/$', views.Show), ## GET show one user 
    url(r'^users/(?P<userID>\d+)/edit$', views.Edit), ## GET show one user
    url(r'^users/(?P<userID>\d+)/update$', views.Update), ## POST edits on that user
    url(r'^users/(?P<userID>\d+)/destroy$', views.Destroy), ## GET then deletes that user
]
