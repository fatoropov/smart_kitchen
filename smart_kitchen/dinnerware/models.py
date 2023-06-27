from django.db import models
from django.urls import reverse


class CategoryDinnerware(models.Model):
    """Модель категорий посуды"""

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
            "dinnerware:dinnerware_list_by_category",
            args=[self.slug],
        )


class Dinnerware(models.Model):
    """Модель посуды"""

    category = models.ForeignKey(
        CategoryDinnerware,
        related_name="dinnerware_category",
        on_delete=models.CASCADE,
        default=None,
    )
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField(blank=True)
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
        return reverse(
            "dinnerware:dinnerware_detail",
            args=[self.id, self.slug],
        )
