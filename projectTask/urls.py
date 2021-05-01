from django.conf.urls import url 
from projectTask import views 
 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [ 
    url(r'^api/projects$', views.project_list),
    url(r'^api/project/(?P<pk>[0-9]+)$', views.project_details),

    url(r'^api/projects/(?P<pk>[0-9]+)/tasks$', views.task_list),
    url(r'^api/projects/(?P<pk>[0-9]+)/tasks/(?P<tk>[0-9]+)$', views.task_details),

    url(r'^api/project/SaveFile$', views.SaveFile)
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)