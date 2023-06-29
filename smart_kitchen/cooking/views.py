# from cart.forms import CartAddDishForm
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render

from .models import Category, Dish


def menu(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    dishes_list = Dish.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        dishes_list = dishes_list.filter(category=category)
    paginator = Paginator(dishes_list, 6)
    page_number = request.GET.get("page", 1)
    try:
        dishes = paginator.page(page_number)
    except PageNotAnInteger:
        dishes = paginator.page(1)
    except EmptyPage:
        dishes = paginator.page(paginator.num_pages)
    # cart_dish_form = CartAddDishForm()

    return render(
        request,
        "cooking/menu.html",
        {
            "category": category,
            "categories": categories,
            "dishes": dishes,
        },
    )
    # 'cart_dish_form': cart_dish_form})


def dish_detail(request, id, slug):
    dish = get_object_or_404(Dish, id=id, slug=slug, available=True)
    # cart_dish_form = CartAddDishForm()
    return render(
        request,
        "cooking/detail.html",
        {
            "dish": dish,
        },
    )
    #    'cart_dish_form': cart_dish_form})
