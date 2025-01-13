from django import forms

from tasty_recipes_app.recipes.models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'

        labels = {
            'cuisine_type': 'Cuisine Type',
            'cooking_time': 'Cooking Time',
            'image_url': 'Image URL',
        }


class RecipeCreateForm(RecipeForm):
    class Meta(RecipeForm.Meta):
        widgets = {
            'ingredients': forms.Textarea(attrs={'placeholder': 'ingredient1, ingredient2, ...'}),
            'instructions': forms.Textarea(attrs={'placeholder': 'Enter detailed instructions here...'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'Optional image URL here...'}),
        }


class RecipeEditForm(RecipeForm):
    pass


class RecipeDeleteForm(RecipeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
