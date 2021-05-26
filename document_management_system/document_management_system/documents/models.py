from django.db import models
from django.conf import settings


class PublicDocumentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='PUBLIC')

class PrivateDocumentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='PRIVATE')

STATUS_CHOICES = (
    ('PUBLIC', 'Public'),
    ('PRIVATE', 'Private')
)

class Document(models.Model):
    user                = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title               = models.CharField(max_length=255)
    document            = models.FileField(upload_to='document/')
    status              = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PUBLIC')
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)

    objects             = models.Manager() # default manager
    public_manager      = PublicDocumentManager() # custom publice manager
    private_manager     = PrivateDocumentManager() # custom private manager    


    def __str__(self):
        return f'{self.title}-#{self.user}'

# group assignment 
class GroupAssignment(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    member = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name=("Group User"))
    document = models.ManyToManyField(Document, verbose_name=("Group Document"))
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
