from django.urls import path
from .views import dish_form, ingredient_form, recipe_find,recipe_form,recipe_detail

urlpatterns = [
                path('ingre/', ingredient_form, name='ingredient-form'),
                path('dish/',dish_form,name='dish-form'),
                path('recipe/',recipe_form,name='recipe-form'),
                path('findrecipe/',recipe_find,name='recipe-find'),
                path('recipe<int:re_id>',recipe_detail,name='recipe-detail')
                ]