from django.shortcuts import render

# Create your views here.

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .models import AnliArcs


def index(request):
    case_list = AnliArcs.objects.all()
    paginator = Paginator(case_list, 5)
    page = request.GET.get('page')
    try:
        case_list = paginator.page(page)
    except PageNotAnInteger:
        case_list = paginator.page(1)
    except EmptyPage:
        case_list = paginator.page(paginator.num_pages)
    context = {
        'case_list': case_list,
    }
    return render(request, 'case/index.html', context)


class Indexview(ListView):
    """docstring for Indexview"""
    model = AnliArcs
    template_name = 'case/index.html'
    context_object_name = 'case_list'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        # 首先获得父类生成的传递给模板的字典
        context = super().get_context_data(**kwargs)
        # 父类生成的字典中已有 paginator、page_obj、is_paginated 这三个模板变量，
        # paginator 是 Paginator 的一个实例，
        # page_obj 是 Page 的一个实例，
        # is_paginated 是一个布尔变量，用于指示是否已分页。
        paginator = context.get('paginator')
        page = context.get('page_obj')
        is_paginated = context.get('is_paginated')
        # 调用自己写的 pagination_data 方法获得显示分页导航条需要的数据
        pagination_data = self.pagination_data(paginator, page, is_paginated)
        # 将分页导航条的模板变量更新到 context 中，注意 pagination_data 方法返回的也是一个字典。
        context.update(pagination_data)
        # 将更新后的 context 返回，以便 ListView 使用这个字典中的模板变量去渲染模板。
        # 注意此时 context 字典中已有了显示分页导航条所需的数据。
        return context

    def pagination_data(self, paginator, page, is_paginated):
        if not is_paginated:
            return{}
        left = []
        right = []
        left_has_more = False
        right_has_more = False
        first = False
        last = False
        page_number = page.number
        total_pages = paginator.num_pages
        page_range = paginator.page_range
        if page_number == 1:
            right = page_range[page_number:page_number + 2]
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
        elif page_number == total_pages:
            left = page_range[(page_number - 3) if (page_number - 3) > 0 else 0:page_number - 1]
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
        else:
            left = page_range[(page_number - 3) if (page_number - 3) > 0 else 0:page_number - 1]
            right = page_range[page_number:page_number + 2]
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True

        data = {
            'left': left,
            'right': right,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more,
            'first': first,
            'last': last,
        }
        return data


def case_detail(request, id):
    case_list = AnliArcs.objects.all()
    curr_case = AnliArcs.objects.get(id=id)
    for index, caseArc in enumerate(case_list):
        if len(case_list) != 1:
            if index == 0:
                previous_index = 'None'
                next_index = index + 1
            elif index == len(case_list) - 1:
                previous_index = index - 1
                next_index = index
            else:
                previous_index = index - 1
                next_index = index + 1
        else:
            previous_index = next_index = 'None'
        # 通过id判断当前文章
        if caseArc.id == id:
            curr_case = caseArc
            if previous_index == 'None':
                previous_caseArc = None
            else:
                previous_caseArc = case_list[previous_index]
            if next_index == 'None':
                next_caseArc = None
            elif next_index == index:
                next_caseArc = None
            else:
                next_caseArc = case_list[next_index]
            break

    context = {
        'caseArc': curr_case,
        'previous_caseArc': previous_caseArc,
        'next_caseArc': next_caseArc,
    }
    return render(request, 'case/detail.html', context)
