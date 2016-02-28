from django.views.generic import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404
from .models.gallery import Gallery


class GalleriesView(TemplateView):
    template_name = 'django_gallery/galleries.html'

    def get_context_data(self, **kwargs):
        context = super(GalleriesView, self).get_context_data(**kwargs)
        galleries_list = Gallery.objects.all()
        # TODO check permissions to galleries

        # TODO add configurable amount of galleries per page
        paginator = Paginator(galleries_list, 12)

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

    def get_context_data(self, **kwargs):
        context = super(GalleryView, self).get_context_data(**kwargs)
        gallery = get_object_or_404(Gallery, slug=self.kwargs.get('slug'))

        # TODO check permissions to photos
        # TODO add configurable amount of photos per page
        paginator = Paginator(gallery.images.all(), 12)

        try:
            page = self.kwargs.get('page')
            images = paginator.page(page)
        except PageNotAnInteger:
            images = paginator.page(1)
        except EmptyPage:
            images = paginator.page(paginator.num_pages)

        context['gallery'] = gallery
        context['images'] = images
        return context

        return context
