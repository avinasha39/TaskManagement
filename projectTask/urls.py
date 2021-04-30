from django.conf.urls import url 
from projectTask import views 
 
urlpatterns = [ 
    url(r'^api/projects$', views.project_list),
    url(r'^api/project/(?P<pk>[0-9]+)$', views.project_details),
    #url(r'^api/projects/(?P<pk>[0-9]+)/tasks$', views.task_list),
    #url(r'^api/projects/(?P<pk>[0-9]+)/tasks/(?P<pk>[0-9]+)$', views.task_details)
]