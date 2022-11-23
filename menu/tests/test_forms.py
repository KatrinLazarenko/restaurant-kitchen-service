from django.test import TestCase

from menu.forms import CookCreationForm, CategorySearchForm, DishSearchForm, CookSearchForm


class FormsTests(TestCase):

    def test_cook_creation_form_is_valid(self):
        form_data = {
            "username": "test_user",
            "password1": "my987test",
            "password2": "my987test",
            "first_name": "First_test",
            "last_name": "Last_test",
            "years_of_experience": 2
        }
        form = CookCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)


class TestSearchForm(TestCase):
    def test_category(self):
        form_data = {"name": "test name"}
        form = CategorySearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_dish(self):
        form_data = {
            "name": "test name",
        }
        form = DishSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_cook(self):
        form_data = {
            "username": "test name",
        }
        form = CookSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
