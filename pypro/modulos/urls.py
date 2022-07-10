from pypro.modulos import views
from django.urls import path

app_name = 'modulos'
urlpatterns = [

    path('<slug:slug>', views.detalhe, name='detalhe'),
    path('aulas/<slug:slug>', views.aula, name='aula'),

]
