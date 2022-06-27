from aperitivos import views
from django.urls import path

app_name = 'aperitivos'
urlpatterns = [
    path('<slug:slug>', views.video, name='video')
]
