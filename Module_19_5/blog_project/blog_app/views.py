from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import *

def post_view(request):
    post_list = Post.objects.all()
    paginate_by = request.GET.get('paginate_by')
    page_num = request.GET.get('page', 1)
    if paginate_by is None:
        paginator = Paginator(post_list, 5)
    else:
        paginator = Paginator(post_list, paginate_by)
    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {'page_obj': page_obj})
