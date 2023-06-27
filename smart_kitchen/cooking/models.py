from django.db import models
from django.urls import reverse


class Menu(models.Model):
    """Модель меню"""

    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=2500, unique=True)

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
    slug = models.SlugField(max_length=200, unique=True)

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
        return reverse(
            "cooking:dish_list_by_category",
            args=[self.slug],
        )


class Dish(models.Model):
    """Модель блюда"""

    category = models.ForeignKey(
        Category, related_name="dishes", on_delete=models.CASCADE, default=None
    )
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    image = models.ImageField(upload_to="dishes/%Y/%m/%d", blank=True)
    description = models.TextField(blank=True)
    composition = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
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
