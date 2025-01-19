from django.shortcuts import render
from django.http import Http404


def index(request):
    template = "blog/index.html"
    return render(request=request, template_name=template, context={})


def post_detail(request, pk):
    posts_map = {}

    if not posts_map.get(pk):
        raise Http404(f"Пост с ID:{pk} не найден!")

    template = "blog/detail.html"
    return render(
        request=request,
        template_name=template,
        context={"post": posts_map[pk]},
    )


def category(request, category_slug):
    template = "blog/category.html"
    return render(
        request=request,
        template_name=template,
        context={"category_slug": category_slug},
    )
