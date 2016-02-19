from django.views.generic import TemplateView


class Galleries(TemplateView):
    template_name = "django_gallery/galleries.html"
