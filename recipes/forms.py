from django import forms
from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            'title',
            'summary',
            'preparation_time',
            'cooking_time',
            'serves',
            'freezable',
            'skill_level',
            'star_rating',
            'main_image',
            'ingredients',
            'instructions',
            'image_a',
            'image_b',
            'image_c',
        ]
