from django.conf.urls import url
from .views import (PageListView,PageView)

urlpatterns = [
    url('^(?P<pk>\d+)/', PageView.as_view(), name='mediapages-detail'),
    url('^$', PageListView.as_view(), name='mediapages-list'),
    ]

