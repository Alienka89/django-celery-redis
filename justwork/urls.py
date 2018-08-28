
from django.conf.urls import url, include
from django.contrib import admin

api_urlpatterns = [
    url(r'^mediapages/', include('justwork.apps.mediapages.urls')),
]
urlpatterns = [
    url(r'^api/', include(api_urlpatterns)),
    url(r'^admin/', admin.site.urls),
    url(r'^tinymce/', include('tinymce.urls')),
]
