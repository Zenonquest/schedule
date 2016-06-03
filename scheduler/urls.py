from django.conf.urls import url
from django.conf.urls import include, url, patterns

from . import views

app_name = 'scheduler'
urlpatterns = [
    # url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^student/(?P<pk>[0-9]+)', views.StudentView.as_view(), name='student detail'),
    url(r'^teacher/(?P<pk>[0-9]+)', views.TeacherView.as_view(), name='teacher detail'),
    url(r'^event/(?P<pk>[0-9]+)', views.EventView.as_view(), name='event detail'),
    url(r'^event', views.EventIndexView.as_view(), name='event list'),

    #api
    url(r'^api/teacher', views.teacher_collection),
    url(r'^api/teacher/(?P<pk>[0-9]+)', views.teacher_element),
    url(r'^api/student', views.student_collection),
    url(r'^api/student/(?P<pk>[0-9]+)', views.student_element),
    url(r'^api/event', views.event_collection),
    url(r'^api/event/(?P<pk>[0-9]+)', views.event_element),
    url(r'^api/testevent', views.event_post),
    url(r'^api/skill', views.skill_collection),
    url(r'^api/skill/(?P<pk>[0-9]+)', views.skill_element),
    url(r'^api/availability', views.availability_collection),
    url(r'^api/availability/(?P<pk>[0-9]+)', views.availability_element),
    url(r'^api/teacher/(?P<teacher_id>[0-9]+)/availability', views.availability_by_teacher),
    url(r'^api/gevent', views.events_get),
    url(r'^api/gevent/(?P<eventId>[A-Za-z0-9_.]+)', views.event_get),

    #socialauth
    url(r'^login', views.login),
    url(r'^home', views.home),
    url(r'^logout', views.logout),
    # url('', include('social.apps.django_app.urls', namespace='social')),

    #marinamele
    # url(r'^$', views.index, name='index'),
    url(r'oauth2callback', views.auth_return, name='return'),
    url(r'oauth2callback2gevents', views.gevents_return, name='gevents_return'),
    url(r'oauth2callback2events', views.events_return, name='events_return'),
    url(r'oauth2callback2postevent', views.post_event_return, name='post_event_return'),
]