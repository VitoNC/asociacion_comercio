from django.db import models


from wagtail.core.models import Page

from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.snippets.models import register_snippet

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



## Modelo para noticias 
@register_snippet # Registrado como snippet
class Noticia(models.Model):
    title = models.CharField('título', max_length=250)
    topic = models.CharField(max_length=20, blank=True)
    subtitle = models.CharField(blank=True, max_length=250)
    url = models.URLField(blank=True)
    date = models.CharField(blank=True, max_length=20)
    body = RichTextField(blank=True)
    imagen = models.URLField(blank=True)


    panels = [
        FieldPanel('title'),
        FieldPanel('subtitle'),
        FieldPanel('date'),
        FieldPanel('body'),
        FieldPanel('imagen'),
        FieldPanel('topic'),
        FieldPanel('url')
    ]

    def __str__(self):
        return f'{self.title} ({self.topic})'

    class Meta:
        verbose_name_plural = 'noticias'
        verbose_name = 'noticia'



class NoticiasIndexPage(Page):
    introduccion = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('introduccion', classname="full")
    ]

    def paginate(self, request, noticias, *args):
        page = request.GET.get('page')

        paginator = Paginator(noticias, 2)

        try:
            pages = paginator.page(page)
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)
        return pages


    def get_context(self, request):
        context = super().get_context(request)

        noticias = self.paginate(request, Noticia.objects.all().order_by('-id'))
        context['noticias'] = noticias
        return context

    subpage_types = []