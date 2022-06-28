from django.shortcuts import render


def video(request, slug):
    videos = {
        'motivacao': {'titulo': 'Vídeo Aperitivo', 'vimeo_id': 'chRPSvKwagU'},
        'instalacao-windows': {'titulo': 'Instalação Windows', 'vimeo_id': 'Zbe2mcmi1MQ'}
    }
    video = videos[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
