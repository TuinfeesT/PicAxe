from django.db import models
from taggit.managers import TaggableManager
from photologue.models import Gallery, Photo


class GalleryExtended(models.Model):
    """
    An extended version of the photologue Gallery model
    """

    # Link back to Photologue's Gallery model.
    gallery = models.OneToOneField(Gallery, related_name='extended')

    # Link to TaggableManager from django-taggit
    tags = TaggableManager(blank=True)

    # Link to parent gallery
    parent = models.ForeignKey('self', null=True, blank=True, related_name='subgalleries')

    def __str__(self):
        return self.gallery.title


class PhotoExtended(models.Model):
    """
    An extended version of the photologue Photo model
    """

    # Link back to Photologue's Photo model
    photo = models.OneToOneField(Photo, related_name='extended')

    # Link to TaggableManager from django-taggit
    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.gallery.title
