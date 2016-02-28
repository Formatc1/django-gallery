from django.views.generic import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models.gallery import Gallery


class GalleriesView(TemplateView):
    template_name = 'django_gallery/galleries.html'

    def get_context_data(self, **kwargs):
        context = super(GalleriesView, self).get_context_data(**kwargs)
        galleries_list = Gallery.objects.all()
        # TODO check permissions

        # TODO add configurable amount of galleries per page
        paginator = Paginator(galleries_list, 1)

        try:
            page = self.kwargs.get('page')
            galleries = paginator.page(page)
        except PageNotAnInteger:
            galleries = paginator.page(1)
        except EmptyPage:
            galleries = paginator.page(paginator.num_pages)

        context['galleries'] = galleries
        return context


class GalleryView(TemplateView):
    template_name = 'django_gallery/gallery.html'
