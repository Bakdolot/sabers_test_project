from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Article


@receiver(pre_save, sender=Article)
def add_short_description(sender, instance, **kwargs):
    """
    this func for adding short description to article when creating
    """
    if instance.pk is None:
        short_description = instance.text[:255]
        instance.short_description = short_description
