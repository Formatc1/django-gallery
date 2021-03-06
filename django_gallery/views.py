from django.views.generic import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, redirect
from .models.gallery import Gallery, Image
from guardian.shortcuts import get_objects_for_user


class GalleriesView(TemplateView):
    template_name = 'django_gallery/galleries.html'

    def get_context_data(self, **kwargs):
        context = super(GalleriesView, self).get_context_data(**kwargs)
        galleries_list = get_objects_for_user(
            user=self.request.user,
            perms='view_gallery',
            klass=Gallery.objects.all()
        )

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

    def get_object(self):
        # TODO check permissions to gallery or return 403
        obj = get_object_or_404(Gallery, slug=self.kwargs.get('slug'))
        return obj

    def get_context_data(self, **kwargs):
        context = super(GalleryView, self).get_context_data(**kwargs)
        gallery = self.get_object()

        images_list = get_objects_for_user(
            user=self.request.user,
            perms='view_image',
            klass=gallery.images.all()
        )
        # TODO add configurable amount of photos per page
        paginator = Paginator(images_list, 12)

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

    def post(self, request, *args, **kwargs):
        gallery = self.get_object()
        images = [Image(
            creator=self.request.user,
            gallery=gallery,
            original_file=image
            ) for image in self.request.FILES.getlist('images')]
        Image.objects.bulk_create(images)
        return redirect('gallery', slug=self.kwargs.get('slug'))
