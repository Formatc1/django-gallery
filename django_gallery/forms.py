from django.forms import ModelForm
from .models.gallery import Gallery


class GalleryForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(GalleryForm, self).__init__(*args, **kwargs)
        self.fields['gallery_image'].queryset = self.instance.images.all()

    class Meta:
        fields = '__all__'
        model = Gallery
