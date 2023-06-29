from django.urls import path

from . import views

app_name = "cooking"

urlpatterns = [
    path(
        "menu/",
        views.menu,
    ),
    path(
        "menu/<slug:menu_slug/",
        views.menu,
        name="menu",
    ),
    path(
        "<slug:category_slug>/",
        views.menu,
        name="dish_list_by_category",
    ),
    path(
        "<int:id>/<slug:slug>/",
        views.dish_detail,
        name="dish_detail",
    ),
]
