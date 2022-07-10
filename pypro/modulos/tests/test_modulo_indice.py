import pytest
from django.urls import reverse
from pypro.modulos.models import Modulo, Aula
from pypro.django_assertions import assert_contains
from model_mommy import mommy
from typing import List


@pytest.fixture()
def modulos(db):
    return mommy.make(Modulo, 2)


@pytest.fixture()
def aulas(modulos):
    aulas = []
    for modulo in modulos:
        aulas.extend(mommy.make(Aula, 3, modulo=modulo))
    return aulas


@pytest.fixture
def resp(client, modulos, aulas):
    resp = client.get(reverse('modulos:indice'))
    return resp


def test_indice_disponivel(resp):
    assert resp.status_code == 200


def test_titulo_do_modulo(resp, modulos: List[Modulo]):
    for modulo in modulos:
        assert_contains(resp, modulo.titulo)


def test_descricao(resp, modulos: Modulo):
    for modulo in modulos:
        assert_contains(resp, modulo.descricao)


def test_publico(resp, modulos: Modulo):
    for modulo in modulos:
        assert_contains(resp, modulo.publico)


def test_titulos_das_aulas(resp, aulas: List[Aula]):
    for aula in aulas:
        assert_contains(resp, aula.titulo)


def test_url_das_aulas(resp, aulas: List[Aula]):
    for aula in aulas:
        assert_contains(resp, aula.get_absolute_url())
