from cart.cart import Cart
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from products.models import Product

from .forms import OrderCreateForm
from .models import Order, OrderItem


def order_create(request):
    cart = Cart(request)
    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item["product"],
                    price=item["price"],
                    quantity=item["quantity"],
                )
            cart.clear()
            return render(request, "orders/order/created.html", {"order": order})
    else:
        form = OrderCreateForm()
    return render(
        request,
        "orders/order/create.html",
        {
            "cart": cart,
            "form": form,
        },
    )


@login_required
def get_orders_history(request):
    client = list(User.objects.filter(id=request.user.id).values())
    orders_list = [
        order
        for order in list(Order.objects.all().values())
        if order["name_id"] == client[0]["id"]
    ]
    orders_id = [id["id"] for id in orders_list]
    orders_item_sum = {}
    orders_items_products = {}

    for i in orders_id:
        orders_item_sum[i] = 0
        orders_items_products[i] = []

    for item in list(OrderItem.objects.all().values()):
        for i in list(orders_item_sum.keys()):
            if item["order_id"] == i:
                orders_item_sum[i] += item["price"] * item["quantity"]
                for n in list(Product.objects.filter(id=item["product_id"])):
                    orders_items_products[i].append(n.name)

    for order in orders_list:
        if int(order["id"]) in list(orders_item_sum.keys()):
            order["price"] = orders_item_sum[int(order["id"])]
            order["products"] = orders_items_products[int(order["id"])]

    paginator = Paginator(orders_list, 10)
    page_number = request.GET.get("page", 1)
    try:
        orders = paginator.page(page_number)
    except PageNotAnInteger:
        orders = paginator.page(1)
    except EmptyPage:
        orders = paginator.page(paginator.num_pages)

    return render(
        request,
        "orders/order/history.html",
        {"orders": orders},
    )
