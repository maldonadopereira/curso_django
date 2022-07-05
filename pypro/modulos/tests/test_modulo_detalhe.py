import pytest
from django.urls import reverse
from pypro.modulos.models import Modulo
from pypro.django_assertions import assert_contains
from model_mommy import mommy


@pytest.fixture()
def modulo(db):
    return mommy.make(Modulo)


@pytest.fixture
def resp(client, modulo):
    resp = client.get(reverse('modulos:detalhe', kwargs={'slug': modulo.slug}))
    return resp


def test_titulo(resp, modulo: Modulo):
    assert_contains(resp, modulo.titulo)


def test_descricao(resp, modulo: Modulo):
    assert_contains(resp, modulo.descricao)

def test_publico(resp, modulo: Modulo):
    assert_contains(resp, modulo.publico)
