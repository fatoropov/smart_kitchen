from cart.forms import CartAddDishForm
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render

from .models import CategoryProducts, Product


def product_list(request, category_slug=None):
    category = None
    categories = CategoryProducts.objects.all()
    products_list = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(CategoryProducts, slug=category_slug)
        products_list = products_list.filter(category=category)
    paginator = Paginator(products_list, 6)
    page_number = request.GET.get("page", 1)
    try:
        products = paginator.page(page_number)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    cart_product_form = CartAddDishForm()

    return render(
        request,
        "products/list.html",
        {
            "category": category,
            "categories": categories,
            "products": products,
            "cart_product_form": cart_product_form,
        },
    )


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddDishForm()
    return render(
        request,
        "products/detail.html",
        {
            "product": product,
            "cart_product_form": cart_product_form,
        },
    )
