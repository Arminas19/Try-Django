from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Recipe, RecipeIngredient
User = get_user_model()


class UserTestCase(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user('Arminas', password='Admin2')
    
    def test_user_pw(self):
        checked = self.user_a.check_password("Admin2")
        self.assertTrue(checked)


class RecipeTestCase(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user('Arminas', password='Admin2')
        self.recipe_a = Recipe.objects.create(user=self.user_a, name='chicken')

    def test_user_count(self):
        qs = User.objects.all()
        self.assertEqual(qs.count(), 1)

    def test_user_recipe_reverse_count(self):
        user = self.user_a
        qs = user.recipe_set.all()
        print(qs)
        self.assertEqual(qs.count(), 1)