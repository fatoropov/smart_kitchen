from decimal import Decimal

from django.conf import settings
from products.models import Product


class Cart:
    def __init__(self, request):
        """Инициализировать корзину"""
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, override_quantity=False):
        """Добавить товар в корзину и обновляет кол-во"""
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {"quantity": 0, "price": str(product.price)}
        if override_quantity:
            self.cart[product_id]["quantity"] = quantity
        else:
            self.cart[product_id]["quantity"] += quantity
        self.save()

    def save(self):
        """Сохраняет изменение сеанса"""
        self.session.modified = True

    def remove(self, product, quantity=1, override_quantity=False):
        """Удалить товар из корзины"""
        product_id = str(product.id)
        if product_id in self.cart:
            if override_quantity or self.cart[product_id]["quantity"] == 1:
                del self.cart[product_id]
            else:
                self.cart[product_id]["quantity"] -= quantity
            self.save()

    def __iter__(self):
        """Получает все товары из БД"""
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]["product"] = product
        for item in cart.values():
            item["price"] = Decimal(item["price"])
            item["total_price"] = item["price"] * item["quantity"]
            yield item

    def __len__(self):
        """Считает кол-во товаров в корзине"""
        return sum(item["quantity"] for item in self.cart.values())

    def get_total_price(self):
        """Возвращает общую цену товаров в магазине"""
        return sum(Decimal(item["price"]) * item["quantity"] for item in self.cart.values())

    def clear(self):
        """Очищает корзину в сеансе"""
        del self.session[settings.CART_SESSION_ID]
        self.save()
