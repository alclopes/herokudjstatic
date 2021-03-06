from __future__ import absolute_import, unicode_literals
from django.db.models.signals import post_delete, post_save
from django.db import models
from django.dispatch import receiver
from django.utils import timezone


class MyImage(models.Model):
    name = models.CharField('Name', max_length=80, unique=True)
    image = models.ImageField(
        upload_to='myimage/images', verbose_name='Image',
        null=False, blank=False)
    created_at = models.DateTimeField('Create at', null=True, auto_now_add=True)


    class Meta:
        verbose_name = 'My Image'
        verbose_name_plural = 'My Images'
        ordering = ['-created_at']

    def __str__(self):
        return self.name


def delete_all(time_ago="all"):
    if time_ago == "all":
        time_ago = timezone.now()
    ok = MyImage.objects.filter(created_at__lte=time_ago).delete()


# Signal to delete the file of image when your register in the database will be deleted.
@receiver(post_delete, sender=MyImage)
def image_post_delete_handler(sender, **kwargs):
    listingImage = kwargs['instance']
    storage, path = listingImage.image.storage, listingImage.image.path
    storage.delete(path)

