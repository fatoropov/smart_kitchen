from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from products.models import Product
from .cart import Cart
from .forms import CartAddDishForm, CartUpdateQuantityDish
from django.contrib import messages

from random import choice


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddDishForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        quantity = cd['quantity']
        messages.success(request,
                         f'Товар - "{product}" ({quantity} шт.) \
                         добавлен в корзину')
        cart.add(product=product,
                 quantity=cd['quantity'],
                 override_quantity=cd['override'])
    else:
        messages.error(request, f'Ошибка \n Товар - {product} не добавлен')
    return redirect('products:product_list')


@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request,
                  'cart/detail.html',
                  {'cart': cart})


def cart_update_plus(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartUpdateQuantityDish(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=1,
                 override_quantity=cd['override'])
    return redirect('cart:cart_detail')


def cart_update_minus(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartUpdateQuantityDish(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.remove(product=product,
                    quantity=1,
                    override_quantity=cd['override'])
    return redirect('cart:cart_detail')


def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart:cart_detail')


# TODO product['category_id'] != 5 Проверить какая категория не должна быть
# т.к. было разделение продукты и напитки
@require_POST
def cart_add_random_product(request):
    cart = Cart(request)
    eda = [product for product in list(Product.objects.all().values())
           if product['category_id'] != 5]
    product_rand = choice(eda)
    product = get_object_or_404(Product, id=product_rand['id'])
    form = CartAddDishForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=1,
                 override_quantity=cd['override'])
        messages.success(request, f'Товар - "{product}" добавлен в корзину')
    else:
        messages.error(request, f'Ошибка \n Товар - {product} не добавлен')
    return redirect('products:product_list')


@require_POST
def cart_add_random_drink(request):
    cart = Cart(request)
    eda = [product for product in list(Product.objects.all().values())
           if product['category_id'] == 5]
    product_rand = choice(eda)
    product = get_object_or_404(Product, id=product_rand['id'])
    form = CartAddDishForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=1,
                 override_quantity=cd['override'])
        messages.success(request, f'Товар - "{product}" добавлен в корзину')
    else:
        messages.error(request, f'Ошибка \n Товар - {product} не добавлен')
    return redirect('products:product_list')
