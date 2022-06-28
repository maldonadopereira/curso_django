from aperitivos import views
from django.urls import path

app_name = 'aperitivos'
urlpatterns = [
    path('', views.indice, name='indice'),
    path('<slug:slug>', views.video, name='video')
]
