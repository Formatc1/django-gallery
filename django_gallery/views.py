from django.views.generic import TemplateView
from django.core.paginator import Paginator
from .models.gallery import Gallery


class GalleriesView(TemplateView):
    template_name = 'django_gallery/galleries.html'

    def get_context_data(self, **kwargs):
        context = super(GalleriesView, self).get_context_data(**kwargs)
        galleries = Gallery.objects.all()
        # TODO: check permissions
        
        paginator = Paginator(galleries, 12)


        return context


class GalleryView(TemplateView):
    template_name = 'django_gallery/gallery.html'
