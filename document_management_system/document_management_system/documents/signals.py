from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from django.utils.text import slugify
from .models import GroupAssignment


@receiver(post_save, sender=GroupAssignment)
def create_group_assignment(sender, instance, created, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)
        instance.save()

@receiver(pre_save, sender=GroupAssignment)
def pre_save_group_assignment(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.name)