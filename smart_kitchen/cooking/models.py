from django.db import models
from django.urls import reverse
from products.models import Product


class Menu(models.Model):
    """Модель меню"""

    name = models.CharField(max_length=250)
    slug = models.SlugField(
        max_length=2500,
        unique=True,
    )

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["name"]),
        ]

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("cooking:menu", args=[self.slug])


class Category(models.Model):
    """Модель категорий меню"""

    menu = models.ForeignKey(
        Menu,
        related_name="categories",
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=200)
    slug = models.SlugField(
        max_length=200,
        unique=True,
    )

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["name"]),
        ]
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("cooking:dish_list_by_category", args=[self.slug])


class Dish(models.Model):
    """Модель блюда"""

    category = models.ForeignKey(
        Category,
        related_name="dishes",
        on_delete=models.CASCADE,
        default=None,
    )
    name = models.CharField(max_length=50)
    slug = models.SlugField(
        max_length=50,
        unique=True,
    )
    image = models.ImageField(
        upload_to="dishes/%Y/%m/%d",
        blank=True,
    )
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["id", "slug"]),
            models.Index(fields=["name"]),
            models.Index(fields=["-created"]),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("cooking:dish_detail", args=[self.id, self.slug])


class DishComposition(models.Model):
    """Состав блюда"""

    dish = models.ForeignKey(
        Dish,
        on_delete=models.CASCADE,
        default=None,
    )
    product = models.ForeignKey(
        Product,
        related_name="dish_product",
        on_delete=models.CASCADE,
    )
    quantity = models.PositiveIntegerField(
        default=1,
        blank=True,
    )
    weigth = models.FloatField(
        blank=True,
    )
    volume = models.PositiveBigIntegerField(
        default=1000,
        blank=True,
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
