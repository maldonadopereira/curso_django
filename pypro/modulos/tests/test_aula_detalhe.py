import pytest
from django.urls import reverse
from pypro.modulos.models import Modulo, Aula
from pypro.django_assertions import assert_contains
from model_mommy import mommy


@pytest.fixture()
def modulo(db):
    return mommy.make(Modulo)


@pytest.fixture()
def aula(modulo):
    return mommy.make(Aula, modulo=modulo)


@pytest.fixture
def resp(client, aula):
    resp = client.get(reverse('modulos:aula', kwargs={'slug': aula.slug}))
    return resp


def test_titulo_da_aula(resp, aula: Aula):
    assert_contains(resp, aula.titulo)


def test_vimeo(resp, aula: Aula):
    assert_contains(resp, f'src="https://www.youtube.com/embed/{ aula.vimeo_id }"')


def test_titulo_do_modulo_breadcrumb(resp, modulo: Modulo):
    assert_contains(resp, f'<li class="breadcrumb-item"><a href="{ modulo.get_absolute_url() }">{ modulo.titulo }</a></li>')
