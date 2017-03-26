from django.conf.urls import url
from . import views


urlpatterns = [
url(r'^$', views.IndexView.as_view(), name='index'),
# ex: /polls/5/
# ex: /polls/5/results/
# ex: /polls/5/vote/
]