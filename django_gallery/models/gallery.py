from os.path import join
from django.db import models
from django.utils.text import slugify
from django.utils.timezone import now
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


def get_storage_path(instance, filename):
    return join('gallery', instance.gallery.slug, filename)


@python_2_unicode_compatible
class Image(models.Model):

    creator = models.ForeignKey(
        User, related_name='images', verbose_name=_('creator'))
    date_added = models.DateTimeField(_('date published'), default=now)
    original_file = models.ImageField(_('image'), upload_to=get_storage_path)
    thumbnail = ImageSpecField(
        source='original_file',
        processors=[ResizeToFill(300, 200)],
        format='JPEG',
        options={'quality': 60}
    )
    large_thumbnail = ImageSpecField(
        source='original_file',
        processors=[ResizeToFill(1920, 1080)],
        format='JPEG',
        options={'quality': 90}
    )
    gallery = models.ForeignKey(
        'Gallery',
        related_name='images',
        verbose_name=_('gallery')
    )

    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')
        permissions = (
            ('view_image', _('Can view image')),
        )

    def __str__(self):
        return '%s/%s' % (self.gallery, self.original_file.name)


@python_2_unicode_compatible
class Gallery(models.Model):

    title = models.CharField(_('title'), max_length=250, unique=True)
    slug = models.SlugField(
        _('title slug'), max_length=250, unique=True, editable=False)
    date_added = models.DateTimeField(_('date published'), default=now)
    description = models.TextField(_('description'), blank=True)
    creator = models.ForeignKey(
        User, related_name='galleries', verbose_name=_('creator'))
    gallery_image = models.OneToOneField(
        Image,
        related_name='gallery_image',
        verbose_name=_('gallery image'),
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = _('Gallery')
        verbose_name_plural = _('Galleries')
        permissions = (
            ('view_gallery', _('Can view gallery')),
        )

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self))
        return super(Gallery, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
