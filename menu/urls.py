from django.urls import path

from menu.views import index, \
    DishListView, DishDetailView, DishCreateView, DishUpdateView, DishDeleteView, CookListView, CookDetailView, \
    CookCreateView, CookExperienceUpdateView, CookDeleteView, toggle_assign_to_dish, CategoryListView, \
    CategoryCreateView, CategoryUpdateView, CategoryDeleteView

urlpatterns = [
    path("", index, name="index"),
    path(
        "categories/",
        CategoryListView.as_view(),
        name="category-list",
    ),
    path(
        "categories/create/",
        CategoryCreateView.as_view(),
        name="category-create",
    ),
    path(
        "categories/<int:pk>/update/",
        CategoryUpdateView.as_view(),
        name="category-update",
    ),
    path(
        "categories/<int:pk>/delete/",
        CategoryDeleteView.as_view(),
        name="category-delete",
    ),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("dishes/create/", DishCreateView.as_view(), name="dish-create"),
    path("dishes/<int:pk>/update/", DishUpdateView.as_view(), name="dish-update"),
    path("dishes/<int:pk>/delete/", DishDeleteView.as_view(), name="dish-delete"),
    path(
        "dishes/<int:pk>/toggle-assign/",
        toggle_assign_to_dish,
        name="toggle-dish-assign",
    ),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path(
        "cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"
    ),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path(
        "cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"
    ),
    path("cooks/create/", CookCreateView.as_view(), name="cook-create"),
    path(
        "cooks/<int:pk>/update/",
        CookExperienceUpdateView.as_view(),
        name="cook-update",
    ),
    path(
        "cooks/<int:pk>/delete/",
        CookDeleteView.as_view(),
        name="cook-delete",
    ),
]

app_name = "menu"
