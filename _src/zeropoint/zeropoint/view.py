from django.shortcuts import render
from news.models import Post
from case.models import AnliArcs
from solution.models import SoluArcs


def index(request):
    news_list = Post.objects.all()[:5]
    case_list = AnliArcs.objects.all()[:5]
    solution_list = SoluArcs.objects.all()[:5]
    context = {
        'news_list': news_list,
        'case_list': case_list,
        'solution_list': solution_list
    }
    return render(request, 'index.html', context)


def product(request):
    context = {}
    return render(request, 'product.html', context)


def solution(request):
    context = {}
    return render(request, 'solution.html', context)


def about(request):
    context = {}
    return render(request, 'about.html', context)


def map(request):
    context = {}
    return render(request, 'map.html', context)
