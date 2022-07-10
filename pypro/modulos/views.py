from django.shortcuts import render

from pypro.modulos import facade


def detalhe(request, slug):
    modulo = facade.encontrar_modulo(slug)
    aulas = facade.listar_aulas_ordenadas(modulo)
    return render(request, 'modulos/modulos_detalhe.html', {'modulo': modulo, 'aulas': aulas})


def aula(request, slug):
    aula = facade.encontrar_aula(slug)
    return render(request, 'modulos/aula_detalhe.html', {'aula': aula})


def indice(request):
    context = {
        'modulos': facade.listar_modulos_com_aulas()
    }
    return render(request, 'modulos/indice.html', context)
