from django.urls import reverse
from django.db import models


class Video(models.Model):
    titulo = models.CharField('Titulo', max_length=32)
    slug = models.SlugField('slug', max_length=32)
    vimeo_id = models.CharField('Vimeo ID', max_length=32)
    created = models.DateTimeField('Criado em: ', auto_now_add=True)
    updated = models.DateTimeField('Atualizado em: ', auto_now=True)

    def __str__(self):
        return f'Video: {self.titulo}'

    def get_absolute_url(self):
        return reverse('aperitivos:video', args=(self.slug,))
