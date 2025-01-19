from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Category, Post


def index(request):
    template = "blog/index.html"
    post_list = (
        Post.objects.filter(
            is_published=True,
            pub_date__lte=timezone.now(),
            category__is_published=True,
        )
        .select_related("category")
        .order_by("-pub_date")
    )

    return render(
        request=request,
        template_name=template,
        context={"post_list": post_list[:5]},
    )


def post_detail(request, pk):
    post = get_object_or_404(
        Post,
        pk=pk,
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True,
    )
    template = "blog/detail.html"
    return render(
        request=request,
        template_name=template,
        context={"post": post},
    )


def category(request, category_slug):
    template = "blog/category.html"
    category_obj = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True,
    )
    post_list = (
        Post.objects.filter(
            is_published=True,
            pub_date__lte=timezone.now(),
            category__is_published=True,
            category=category_obj,
        )
        .select_related("category")
        .order_by("-pub_date")
    )

    return render(
        request=request,
        template_name=template,
        context={"category": category_obj, "post_list": post_list},
    )
