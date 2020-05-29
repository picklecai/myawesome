from django.shortcuts import render


def index(request):
    context = {}
    '''
    context['hello'] = 'Hello world!'
    '''
    return render(request, 'index.html', context)
