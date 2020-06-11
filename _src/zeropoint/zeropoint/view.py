from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from news.models import Post


def index(request):
    news_list = Post.objects.all()
    paginator = Paginator(news_list, 5)
    page = request.GET.get('page')
    try:
        news_list = paginator.page(page)
    except PageNotAnInteger:
        news_list = paginator.page(1)
    except EmptyPage:
        news_list = paginator.page(paginator.num_pages)
    context = {
        'news_list': news_list
    }
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
