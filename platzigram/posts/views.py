'''
Vistas de los posts.
La vista es la lógica de traer los datos.
'''

from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

posts = [
        {
            'name': 'Mont Blanc',
            'user': 'Diego',
            'timestamp': datetime.now().strftime('%b, %dth, %Y - %H:%M hrs'),
            'picture': 'https://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-694540.jpg'
        },
        {
            'name': 'Mont Blanc',
            'user': 'Diego',
            'timestamp': datetime.now().strftime('%b, %dth, %Y - %H:%M hrs'),
            'picture': 'https://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-694540.jpg'
        },
        {
            'name': 'Mont Blanc',
            'user': 'Diego',
            'timestamp': datetime.now().strftime('%b, %dth, %Y - %H:%M hrs'),
            'picture': 'https://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-694540.jpg'
        }
    ]


def list_posts(request):
    content = []
    for post in posts:
        content.append(
            """
            <p>{name}</p>
            <p>{user}</p>
            <p>{timestamp}</p>
            <figure><img src="{picture}"/></figure>
            """.format(**post)
        )
    
    return HttpResponse(content)

def list_posts2(request):
    return render(request, 'feed.html',  {'posts': posts})


# Create your views here.
