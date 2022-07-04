from django.db import models
from ordered_model.models import OrderedModel


class Modulo(OrderedModel):
    titulo = models.CharField('Titulo', max_length=64)
    publico = models.TextField('Público')
    descricao = models.TextField('Descrição')

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return self.titulo
