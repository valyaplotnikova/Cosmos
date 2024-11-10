from django.db import models
from filer.fields.image import FilerImageField


class SliderImage(models.Model):
    title = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='название изображения'
    )
    image = FilerImageField(
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='image',
        verbose_name='изображение'
    )
    description = models.TextField(
        blank=True,
        verbose_name='описание изображения'
    )
    my_order = models.PositiveIntegerField(
        default=0,
        db_index=True,
        blank=False,
        null=False
    )

    class Meta:
        verbose_name = 'изображение'
        verbose_name_plural = 'изображения'
        ordering = ['my_order']

    def __str__(self):
        return self.title
