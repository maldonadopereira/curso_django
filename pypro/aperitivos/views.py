from django.shortcuts import render, get_object_or_404
from .models import Video


def indice(request):
    videos = Video.objects.order_by('created').all()
    return render(request, 'aperitivos/indice.html', context={'videos': videos})


def video(request, slug):
    video = get_object_or_404(Video, slug=slug)
    return render(request, 'aperitivos/video.html', context={'video': video})