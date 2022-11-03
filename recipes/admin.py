from django.contrib.auth import get_user_model
from django.contrib import admin
from .models import Recipe, RecipeIngredient, RecipeIngredientImage
# Register your models here.

User = get_user_model()
# admin.site.unregister(User)

admin.site.register(RecipeIngredientImage)

# class RecipeInline(admin.StackedInline):
#     model = Recipe
#     extra = 0

# class UserAdmin(admin.ModelAdmin):
#     inlines = [RecipeInline]
#     list_display = ['username']


# admin.site.register(User, UserAdmin)


class RecipeIngredientInline(admin.StackedInline):
    model = RecipeIngredient
    extra = 0
    readonly_fields = ['quantity_as_float', 'as_mks', 'as_imperial']
    # fields = ['name', 'quantity', 'unit', 'direction']


class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]
    list_display = ['name', 'user']
    readonly_fields = ['timestamp', 'updated']
    raw_id_fields = ["user"]

admin.site.register(Recipe, RecipeAdmin)