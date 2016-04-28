from django.conf.urls import url

from . import views

app_name = 'scheduler'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^student/(?P<pk>[0-9]+)/$', views.StudentView.as_view(), name='student detail'),
    url(r'^teacher/(?P<pk>[0-9]+)/$', views.TeacherView.as_view(), name='teacher detail'),
    url(r'^event/(?P<pk>[0-9]+)/$', views.EventView.as_view(), name='event detail'),
    url(r'^event/$', views.EventIndexView.as_view(), name='event list'),

    #api
    url(r'^api/v1/teachers/$', views.teacher_collection),
    url(r'^api/v1/teachers/(?P<pk>[0-9]+)/$', views.teacher_element),
    url(r'^api/v1/events/$', views.event_collection)
]