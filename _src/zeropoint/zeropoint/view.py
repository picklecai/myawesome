from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'index.html', context)


def product(request):
    context = {}
    return render(request, 'product.html', context)


def solution(request):
    context = {}
    return render(request, 'solution.html', context)


def case(request):
    context = {}
    return render(request, 'case.html', context)


def about(request):
    context = {}
    return render(request, 'about.html', context)


def map(request):
    context = {}
    return render(request, 'map.html', context)
