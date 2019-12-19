from django.conf.urls import url
from todo.views import todoadd,todoedit,tododelete,todolist,about

#call CRUD operations

urlpatterns=[
    url(r'^$',todolist,name='todolist'),
    url(r'^add/$',todoadd,name='todoadd'),
    url(r'^edit/(?P<pk>\d+)$',todoedit,name='todoedit'),
    url(r'^delete/(?P<pk>\d+)$',tododelete,name='tododelete'),
    url(r'^about/$',about,name='about'),
    ]
