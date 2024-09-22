from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def user_can_make(self, user):
        recipes = []
        for recipe in Recipe.objects.iterator():
            if recipe.user_can_make(user):
                for ri in RecipeIngredient.objects.filter(recipe=recipe):
                    if ri.ingredient.id == self.id:
                        recipes.append(recipe)
        return recipes

    def __str__(self):
        return str(self.name)

    def __eq__(self, other):
        return self.id == other.id

    def __lt__(self, other):
        return self.id < other.id

    def __gt__(self, other):
        return self.id > other.id