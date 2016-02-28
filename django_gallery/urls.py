from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<page>\d+/)?$', views.GalleriesView.as_view(), name='galleries'),
    url(r'^gallery/(?P<slug>[-\w]+)/(?P<page>\d+/)?$',
        views.GalleryView.as_view(), name='gallery'),
    # url(r'^image/(?P<id>\d+)/$', views.ImageView.as_view(), name='image'),
]
