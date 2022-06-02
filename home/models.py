from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


class HomePage(Page):
    body = RichTextField(blank=True)
    img = models.CharField(blank=True, max_length=200)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        FieldPanel('img')
    ]