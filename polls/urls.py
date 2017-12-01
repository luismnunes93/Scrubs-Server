from django.conf.urls import url

from . import views
from . import api

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^api/v1/question/$', api.QuestionList.as_view()),
    url(r'^api/v1/choice/$', api.ChoiceList.as_view()),
]
