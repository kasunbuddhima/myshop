from django.db import models
from oscar.apps.catalogue.abstract_models import AbstractProduct


class Product(AbstractProduct):
    # altered fields in AbstractProduct model
    is_active = models.BooleanField(default=False, help_text='indicates whether products is active or not')
    short_info = models.TextField(blank=True, null=True, help_text='short details about product')


from oscar.apps.catalogue.models import *




