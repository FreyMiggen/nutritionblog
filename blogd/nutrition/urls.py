from django.urls import path
from .views import ingredient_form

urlpatterns = [
                path('', ingredient_form, name='ingredient-form'),]