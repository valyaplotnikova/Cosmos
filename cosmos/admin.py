from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin

from cosmos.models import SliderImage


@admin.register(SliderImage)
class SliderImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('my_order', 'title', 'image', 'description')
