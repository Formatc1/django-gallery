from django.contrib import admin
from .models.gallery import Gallery, Image
from .forms import GalleryForm
from guardian.admin import GuardedModelAdmin


class GalleryAdmin(GuardedModelAdmin):
    form = GalleryForm


class ImageAdmin(GuardedModelAdmin):
    pass

admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Image, ImageAdmin)
