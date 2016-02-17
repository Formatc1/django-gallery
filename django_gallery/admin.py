from django.contrib import admin
from .models.Gallery import Gallery, Image
from guardian.admin import GuardedModelAdmin
# from .models.UserGroup import Group


class GalleryAdmin(GuardedModelAdmin):
    pass


class ImageAdmin(GuardedModelAdmin):
    pass

admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Image, ImageAdmin)
# admin.site.register(Group)
