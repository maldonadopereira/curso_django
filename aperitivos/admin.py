from django.contrib.admin import ModelAdmin, register
from aperitivos.models import Video


@register(Video)
class VideoAdmin(ModelAdmin):
    list_display = ('id', 'titulo', 'slug', 'created', 'vimeo_id')
    list_display_links = ('titulo',)
    ordering = ('created',)
    prepopulated_fields = {'slug': ('titulo',)}
