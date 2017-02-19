from django.shortcuts import get_object_or_404, render, redirect
from .models import Recipe
from .forms import RecipeForm


def index(request):
    recipes = Recipe.objects.all()
    context = {'recipes': recipes}
    return render(request, 'recipes/index.html', context)


def detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if recipe.ingredients:
        ingredients = recipe.ingredients.split('#')[1:]
    else:
        ingredients = []
    if recipe.instructions:
        instructions = recipe.instructions.split('#')[1:]
    else:
        instructions = []
    context = {'recipe': recipe, 'ingredients': ingredients, 'instructions': instructions}
    return render(request, 'recipes/detail.html', context)


def create(request):
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.save()
            return redirect('detail', recipe_id=recipe.id)
    else:
        form = RecipeForm()

    return render(request, 'recipes/edit.html', {'form': form})


def edit(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)

    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.save()
            return redirect('detail', recipe_id=recipe.id)
    else:
        form = RecipeForm(instance=recipe)

    return render(request, 'recipes/edit.html', {'form': form})
