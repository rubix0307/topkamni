from django.shortcuts import render

# Create your views here.

def index(request):

    context = {
        'title': 'TopKamni.ru: сайт о драгоценных камнях',
    }
    return render(request, 'main/index.html', context)