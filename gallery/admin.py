from django.contrib import admin
from django.contrib.admin.options import InlineModelAdmin
from django.contrib.sites.models import Site
from photologue.admin import GalleryAdmin as GalleryAdminDefault
from photologue.admin import PhotoAdmin as PhotoAdminDefault
from photologue.models import Gallery, Photo
from taggit.models import Tag
from .models import GalleryExtended, PhotoExtended


class GalleryExtendedInline(InlineModelAdmin):
    template = 'admin/edit_inline/fullinline.html'
    model = GalleryExtended
    can_delete = False


class GalleryAdmin(GalleryAdminDefault):

    """Define our new one-to-one model as an inline of Photologue's Gallery model."""

    inlines = [
        GalleryExtendedInline,
    ]

admin.site.unregister(Gallery)
admin.site.register(Gallery, GalleryAdmin)


class PhotoExtendedInline(InlineModelAdmin):
    template = 'admin/edit_inline/fullinline.html'
    model = PhotoExtended
    can_delete = False


class PhotoAdmin(PhotoAdminDefault):

    """Define our new one-to-one model as an inline of Photologue's Photo model."""

    inlines = [
        PhotoExtendedInline,
        ]

admin.site.unregister(Photo)
admin.site.register(Photo, PhotoAdmin)

# Remove Site support from admin
admin.site.unregister(Site)

# Remove direct Tags support from admin
admin.site.unregister(Tag)
