from django.db import models
from django import forms

from modelcluster.fields import ParentalManyToManyField
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel


from wagtail.snippets.models import register_snippet

from wagtail.search import index


# Create your models here.



class ComercioIndexPage(Page):
    introduccion = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('introduccion', classname="full")
    ]

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)

        categoria = request.GET.get('categoria')
        
        if categoria == 'alimentacion':
            entradas = ComercioAliPage.objects.live().order_by('-first_published_at')
        elif categoria == 'hosteleria':
            entradas = ComercioHosPage.objects.live().order_by('-first_published_at')
        elif categoria == 'moda':
            entradas = ComercioModPage.objects.live().order_by('-first_published_at')
        elif categoria == 'servicios':
            entradas = ServiciosPage.objects.live().order_by('-first_published_at')
        else:
            entradas = self.get_children().live().order_by('-first_published_at')

        context['blogpages'] = entradas

        return context

    subpage_types = ['ComercioAliPage', 'ComercioHosPage', 'ComercioModPage', 'ServiciosPage']



# Modelo Página Alimentación
class ComercioAliPage(Page):

    descripcion = models.CharField(blank=True, max_length=200)
    coord = models.CharField(blank=True, max_length=20)
    categories = ParentalManyToManyField('comercios.ComercioCategory', blank=True)
    imagen = models.URLField(blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('title'),
        index.SearchField('descripcion'),
    ]

    content_panels = Page.content_panels + [
           
        FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
            
        FieldPanel('coord'),
        FieldPanel('imagen'),
        FieldPanel('descripcion', classname="full"),

    ]

    parent_page_types = ['comercios.ComercioIndexPage']
    subpage_types = []

# Modelo Página Hosteleria
class ComercioHosPage(Page):


    parent_page_types = ['comercios.ComercioIndexPage']
    subpage_types = []

# Modelo Página Moda
class ComercioModPage(Page):


    parent_page_types = ['comercios.ComercioIndexPage']
    subpage_types = []

# Modelo Página Servicios
class ServiciosPage(Page):


    parent_page_types = ['comercios.ComercioIndexPage']
    subpage_types = []


## Modelo para productos
@register_snippet # Registrado como snippet
class Producto(models.Model):
    name = models.CharField('name', max_length=250)
    url = models.URLField(blank=True)
    description = models.CharField(max_length=1000, blank=True)
    image = models.URLField()
    price = models.CharField(max_length=30, blank=True)

    panels = [
        FieldPanel('name'),
        FieldPanel('description'),
        FieldPanel('url'),
        FieldPanel('image'),
        FieldPanel('price'),
    ]

    def __str__(self):
        return f'{self.name} ({self.price}€)'




@register_snippet
class ComercioCategory(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    panels = [
        FieldPanel('name'),
        ImageChooserPanel('icon'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categorías de comercio'
        verbose_name = 'categoría de comercio'