from django.core.exceptions import ValidationError
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
        self.recipe_b = Recipe.objects.create(user=self.user_a, name='Chicken Tacos')
        self.recipe_ingredient_a = RecipeIngredient.objects.create(recipe=self.recipe_a, name='chicken', quantity='1/2', unit='pound')


    def test_user_count(self):
        qs = User.objects.all()
        self.assertEqual(qs.count(), 1)

    def test_user_recipe_reverse_count(self):
        user = self.user_a
        qs = user.recipe_set.all()
        self.assertEqual(qs.count(), 2)

    def test_user_recipe_forward_count(self):
        user = self.user_a
        qs = Recipe.objects.filter(user=user)
        self.assertEqual(qs.count(), 2)
    
    def test_recipe_ingredient_reverse_count(self):
        recipe = self.recipe_a
        qs = recipe.recipeingredient_set.all()
        self.assertEqual(qs.count(), 1)
    
    def test_recipe_ingredientcount(self):
        recipe = self.recipe_a
        qs = RecipeIngredient.objects.filter(recipe=recipe)
        self.assertEqual(qs.count(), 1)
    
    def test_user_two_level_relation(self):
        user = self.user_a
        qs = RecipeIngredient.objects.filter(recipe__user=user)
        self.assertEqual(qs.count(), 1)
    
    def test_user_two_level_relation_reverse(self):
        user = self.user_a
        recipeingredients_ids = list(user.recipe_set.all().values_list('recipeingredient__id', flat=True))
        qs = RecipeIngredient.objects.filter(id__in=recipeingredients_ids)
        self.assertEqual(qs.count(), 1)

    def test_unit_measure_validation(self):
        invalid_unit = 'kg'
        ingredient = RecipeIngredient(
            name='New',
            quantity=10,
            recipe=self.recipe_a,
            unit=invalid_unit
        )
        ingredient.full_clean()

    def test_unit_measure_validation_error(self):
        invalid_unit = 'nada'
        with self.assertRaises(ValidationError):
            ingredient = RecipeIngredient(
                name='New',
                quantity=10,
                recipe=self.recipe_a,
                unit=invalid_unit
            )
            ingredient.full_clean()
