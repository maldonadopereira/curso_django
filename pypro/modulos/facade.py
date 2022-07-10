from pypro.modulos.models import Modulo, Aula
from typing import List
from django.db.models.query import Prefetch


def listar_metodos_ordenados() -> List[Modulo]:
    '''
    Lista módulos ordenados por títulos
    '''
    return list(Modulo.objects.order_by('order').all())


def encontrar_modulo(slug: str):
    return Modulo.objects.get(slug=slug)


def listar_aulas_ordenadas(modulo: Modulo):
    return modulo.aula_set.order_by('order').all()


def encontrar_aula(slug: str):
    return Aula.objects.select_related('modulo').get(slug=slug)


def listar_modulos_com_aulas():
    aulas_ordenadas = Aula.objects.order_by('order')
    return Modulo.objects.order_by('order').prefetch_related(
        Prefetch('aula_set', queryset=aulas_ordenadas, to_attr='aulas')
    ).all()
