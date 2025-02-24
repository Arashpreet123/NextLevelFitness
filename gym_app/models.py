from django.db import models

# Create your models here.
class CarouselImage(models.Model):
    image = models.ImageField(default='fallback.png', blank=True,upload_to='carousel/')
    alt_text = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.alt_text or "Carousel Image"