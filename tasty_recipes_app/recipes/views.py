from django.shortcuts import render, redirect

from tasty_recipes_app.core.utils import get_last_profile
from tasty_recipes_app.recipes.forms import RecipeCreateForm, RecipeEditForm, RecipeDeleteForm
from tasty_recipes_app.recipes.models import Recipe


def show_catalogue(request):
    profile = get_last_profile()
    recipes = Recipe.objects.all()

    context = {
        'profile': profile,
        'recipes': recipes,
    }
    return render(request, 'common/catalogue.html', context)


def create_recipe(request):
    profile = get_last_profile()

    if request.method == 'POST':
        form = RecipeCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    form = RecipeCreateForm()
    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'recipes/create-recipe.html', context)


def details_recipe(request, recipe_id):
    profile = get_last_profile()
    recipe = Recipe.objects.get(pk=recipe_id)
    ingredients = recipe.ingredients.split(', ')

    context = {
        'profile': profile,
        'recipe': recipe,
        'ingredients': ingredients,
    }
    return render(request, 'recipes/details-recipe.html', context)


def edit_recipe(request, recipe_id):
    profile = get_last_profile()
    recipe = Recipe.objects.get(pk=recipe_id)

    if request.method == 'POST':
        form = RecipeEditForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    form = RecipeEditForm(instance=recipe)
    context = {
        'profile': profile,
        'recipe': recipe,
        'form': form,
    }

    return render(request, 'recipes/edit-recipe.html', context)


def delete_recipe(request, recipe_id):
    profile = get_last_profile()
    recipe = Recipe.objects.get(pk=recipe_id)

    if request.method == 'POST':
        recipe.delete()
        return redirect('catalogue')
    form = RecipeDeleteForm(instance=recipe)
    context = {
        'profile': profile,
        'form': form,
        'recipe': recipe,
    }

    return render(request, 'recipes/delete-recipe.html', context)
