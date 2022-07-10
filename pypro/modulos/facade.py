from pypro.modulos.models import Modulo, Aula
from typing import List


def listar_metodos_ordenados() -> List[Modulo]:
    '''
    Lista módulos ordenados por títulos
    '''
    return list(Modulo.objects.order_by('order').all())


def encontrar_modulo(slug: str):
    return Modulo.objects.get(slug=slug)


def listar_aulas_ordenadas(modulo:Modulo):
    '''
    Lista aulas ordenados por modulo
    '''
    return modulo.aula_set.order_by('order').all()


def encontrar_aula(slug: str):
    return Aula.objects.get(slug=slug)