from django.db import models

from datetime import datetime

from imagekit.models import ImageSpec
from imagekit.processors import resize

class EventImage(models.Model):
    title = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='event-images')
    caption = models.TextField(blank=True)
    default_image = ImageSpec(
        [resize.Fit(500, 500),],
        image_field='image',
        format='JPEG',
        options={'quality': 90}
    )

    def __unicode__(self):
        return self.title

    def save(self):
        if not self.title:
            self.title = self.image.name
        super(EventImage, self).save()

class Event(models.Model):
    title = models.CharField(max_length=255)
    details = models.TextField(blank=True)
    venue = models.CharField(max_length=255)
    url = models.URLField(blank=True, null=True)
    image = models.ForeignKey(EventImage, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return self.title + ' - ' + str(self.start_time)