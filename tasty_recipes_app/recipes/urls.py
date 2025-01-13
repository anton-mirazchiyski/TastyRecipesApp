from django.urls import path, include

from tasty_recipes_app.recipes.views import show_catalogue, create_recipe, details_recipe, edit_recipe, delete_recipe

urlpatterns = [
    path('catalogue/', show_catalogue, name='catalogue'),
    path('create/', create_recipe, name='create recipe'),
    path('<int:recipe_id>/', include([
        path('details/', details_recipe, name='details recipe'),
        path('edit/', edit_recipe, name='edit recipe'),
        path('delete/', delete_recipe, name='delete recipe'),
    ])),
]
