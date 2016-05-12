from django.conf.urls import url

from . import views

app_name = 'scheduler'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^student/(?P<pk>[0-9]+)/$', views.StudentView.as_view(), name='student detail'),
    url(r'^teacher/(?P<pk>[0-9]+)/$', views.TeacherView.as_view(), name='teacher detail'),
    url(r'^event/(?P<pk>[0-9]+)/$', views.EventView.as_view(), name='event detail'),
    url(r'^event/$', views.EventIndexView.as_view(), name='event list'),
    
    #oauth2
    # url(r'^user/$', views.UserViewSet, name='user list'),
    # url(r'^group/$', views.GroupViewSet, name='group list'),

    #api
    url(r'^api/teacher/$', views.teacher_collection),
    url(r'^api/teacher/(?P<pk>[0-9]+)/$', views.teacher_element),
    url(r'^api/student/$', views.student_collection),
    url(r'^api/student/(?P<pk>[0-9]+)/$', views.student_element),
    url(r'^api/event/$', views.event_collection),
    url(r'^api/event/(?P<pk>[0-9]+)/$', views.event_element),
    url(r'^api/skill/$', views.skill_collection),
    url(r'^api/skill/(?P<pk>[0-9]+)/$', views.skill_element),

]