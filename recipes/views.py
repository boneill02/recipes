from django.shortcuts import get_object_or_404, render
from .models import Recipe, Ingredient
from .app import available_recipes

def index(request):
    context = {
        "recipes": available_recipes(request.user),
        "username": request.user.username
    }
    return render(request, "recipes/index.html", context)


def available_recipes_view(request):
    context = {
        "recipes": available_recipes(request.user),
        "username": request.user.username
    }
    return render(request, "recipes/available_recipes.html", context)

def available_recipes_with_ingredient_view(request, ingredient_id):
    """
    Show recipes user has all ingredients for that includes ingredient_id
    """
    pass

def ingredient_view(request, ingredient_id):
    recipe = get_object_or_404(Ingredient, pk=ingredient.id)
    return render(request, "recipes/ingredient.html", {"ingredient": ingredient})

def recipe_view(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, "recipes/recipe.html", {"recipe": recipe})