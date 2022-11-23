from django.contrib.auth import get_user_model

from django.test import TestCase

from menu.models import Category, Dish


class DishTests(TestCase):
    def setUp(self) -> None:
        self.category = Category.objects.create(name="name1")

    def test_dish_str(self):
        dish = Dish.objects.create(
            name="test_name",
            description="test_description",
            price="100.01",
            category=self.category
        )
        self.assertEqual(str(dish), f"{dish.name} - {dish.price}")

    def test_category_str(self):
        self.assertEqual(str(self.category), self.category.name)

    def test_cook_str(self):
        cook = get_user_model().objects.create_user(
            username="name",
            password="name310293",
            first_name="test_name",
            last_name="test_surname",
        )
        self.assertEqual(
            str(cook),
            f"{cook.username} ({cook.first_name} {cook.last_name})"
        )

    def test_assign_years_of_experience(self):
        username = "test_name"
        password = "test92837"
        years_of_experience = 33
        cook = get_user_model().objects.create_user(
            username=username,
            password=password,
            years_of_experience=years_of_experience
        )
        self.assertEqual(cook.username, username)
        self.assertTrue(cook.check_password(password))
        self.assertEqual(cook.years_of_experience, years_of_experience)
