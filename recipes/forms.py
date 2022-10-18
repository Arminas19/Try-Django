from django import forms
from .models import Recipe, RecipeIngredient


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe 
        fields = ['name', 'desciption', 'direction']


class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient 
        fields = ['name', 'quantity', 'unit']