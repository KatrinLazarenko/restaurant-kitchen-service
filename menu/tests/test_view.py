from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from menu.models import Category, Dish, Cook

CATEGORY_URL = reverse("menu:category-list")
DISH_URL = reverse("menu:dish-list")
COOK_URL = reverse("menu:cook-list")


class PuPublicTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_category_login_required(self):
        res = self.client.get(CATEGORY_URL)
        self.assertNotEqual(res.status_code, 200)

    def test_dish_login_required(self):
        res = self.client.get(DISH_URL)
        self.assertNotEqual(res.status_code, 200)

    def test_cook_login_required(self):
        res = self.client.get(COOK_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateTests(TestCase):
    def setUp(self) -> None:
        self.cook = get_user_model().objects.create_user(
            "test",
            "password123"
        )
        self.client.force_login(self.cook)
        self.category = Category.objects.create(name="test_category")

    def test_retrieve_category(self):
        Category.objects.create(name="test1")
        Category.objects.create(name="test2")
        response = self.client.get(CATEGORY_URL)
        categories = Category.objects.all()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["category_list"]),
            list(categories)
        )
        self.assertTemplateUsed(response, "menu/category_list.html")

    def test_retrieve_dish(self):
        Dish.objects.create(
            name="test_name1",
            description="test_description1",
            price="100.01",
            category=self.category,
        )
        Dish.objects.create(
            name="test_name2",
            description="test_description2",
            price="200.02",
            category=self.category,
        )
        response = self.client.get(DISH_URL)
        Dish.objects.all()
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "menu/dish_list.html")

    def test_retrieve_cook(self):
        Cook.objects.create_user(
            username="name_1",
            password="name112345",
            first_name="test_name1",
            last_name="test_surname1",
            years_of_experience=11
        )
        Cook.objects.create_user(
            username="name_2",
            password="name209876",
            first_name="test_name2",
            last_name="test_surname2",
            years_of_experience=22
        )
        response = self.client.get(COOK_URL)
        Cook.objects.all()
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "menu/cook_list.html")
