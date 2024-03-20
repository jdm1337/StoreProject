from django.shortcuts import get_object_or_404, render

from .models import Item, ItemTag
from .paginator import paginator


def store(request):
    items = Item.objects.filter(is_available=True)
    category_slug = request.GET.get('category')
    sort_by = request.GET.get('sort_by')

    if category_slug:
        items = items.filter(tags__slug=category_slug)

    if sort_by:
        if sort_by == 'price_asc':
            items = items.order_by('price')
        elif sort_by == 'price_desc':
            items = items.order_by('-price')

    tags = ItemTag.objects.all()  # Получаем все теги

    context = {
        'page_obj': paginator(request, items, 9),
        'tags': tags,  # Передаём теги в контекст
        'range': [*range(1, 7)],  # For random css styles
    }

    return render(request, 'store/main_page.html', context)


def item_details(request, item_slug):
    item = get_object_or_404(Item, slug=item_slug)
    context = {
        'item': item,
    }
    return render(request, 'store/item_details.html', context)


def tag_details(request, slug):
    tag = get_object_or_404(ItemTag, slug=slug)
    items = Item.objects.filter(tags__in=[tag])
    context = {
        'tag': tag,
        'page_obj': paginator(request, items, 3),
    }
    return render(request, 'store/tag_details.html', context)


def tag_list(request):
    tags = ItemTag.objects.all()
    context = {
        'page_obj': paginator(request, tags, 6),
    }
    return render(request, 'store/tag_list.html', context)
