from django.forms import ModelForm
from .models.gallery import Gallery, Image


class GalleryForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(GalleryForm, self).__init__(*args, **kwargs)
        self.fields['gallery_image'].queryset = self.instance.images.all()

    class Meta:
        model = Gallery
        fields = '__all__'


class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = '__all__'
