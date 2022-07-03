from django.shortcuts import render

# from pypro.modulos import facade


def home(request):
    return render(request, 'base/home.html', {'contato_email': 'ramalho@python.pro.br', })
