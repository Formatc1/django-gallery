from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<page>\d+/)?$', views.Galleries.as_view(), name='galleries'),
    url(r'^gallery/(?P<slug>[-\w]+)/(?P<page>\d+/)?$',
        views.Gallery.as_view(), name='gallery'),
    # url(r'^image/(?P<id>\d+)/$', views.Image.as_view(), name='image'),
]
